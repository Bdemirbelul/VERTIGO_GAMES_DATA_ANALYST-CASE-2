

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
import warnings
import gzip
from datetime import datetime, timedelta
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from scipy import stats
warnings.filterwarnings('ignore')

sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (14, 8)
plt.rcParams['font.size'] = 10

PROJECT_ROOT = Path(__file__).parent.parent
DATA_DIR = PROJECT_ROOT / "data" / "raw"
OUTPUT_DIR = PROJECT_ROOT / "outputs"
FIGURES_DIR = OUTPUT_DIR / "figures"
REPORTS_DIR = OUTPUT_DIR / "reports"

FIGURES_DIR.mkdir(parents=True, exist_ok=True)
REPORTS_DIR.mkdir(parents=True, exist_ok=True)


def load_data(data_dir):
    """
    Verilen klasördeki tüm .csv.gz dosyalarını birleştirir.
    (Not: Büyük veri olduğu için tek yerde toplamak işimizi kolaylaştırıyor.)
    """
    data_dir = Path(data_dir)
    csv_files = sorted(data_dir.glob("*.csv.gz"))

    if not csv_files:
        raise FileNotFoundError(f"No CSV.gz files found in {data_dir}")

    dfs = []
    for file_path in csv_files:
        df = pd.read_csv(file_path, compression='gzip')
        dfs.append(df)

    df = pd.concat(dfs, ignore_index=True)

    df['event_date'] = pd.to_datetime(df['event_date'])
    df['install_date'] = pd.to_datetime(df['install_date'])

    return df


def analyze_first_day_engagement(df):
    # İlk gün kullanıcı davranışlarını analiz ediyoruz. (Oyuna giriş kalitesi diyebiliriz.)

    first_day_data = df[df['event_date'] == df['install_date']].copy()

    first_day_metrics = first_day_data.groupby('user_id').agg({
        'total_session_count': 'sum',
        'total_session_duration': 'sum',
        'match_start_count': 'sum',
        'match_end_count': 'sum',
        'victory_count': 'sum',
        'defeat_count': 'sum',
        'iap_revenue': 'sum',
        'ad_revenue': 'sum'
    }).reset_index()

    # Kullanıcının ilk günde oyuna ne kadar "tutunduğunu" daha iyi görmek için ek metrikler
    first_day_metrics['avg_session_duration'] = (
        first_day_metrics['total_session_duration'] /
        first_day_metrics['total_session_count'].replace(0, np.nan)
    )
    first_day_metrics['win_rate'] = (
        first_day_metrics['victory_count'] /
        (first_day_metrics['victory_count'] + first_day_metrics['defeat_count']).replace(0, np.nan)
    )
    first_day_metrics['total_revenue'] = (
        first_day_metrics['iap_revenue'] + first_day_metrics['ad_revenue']
    )
    first_day_metrics['match_completion_rate'] = (
        first_day_metrics['match_end_count'] /
        first_day_metrics['match_start_count'].replace(0, np.nan)
    )

    first_day_metrics = first_day_metrics.fillna(0)

    # Segmentasyon için sklearn kullanıyoruz  kullanıcıları davranış kalıplarına göre gruplıyoruz.
    scaler = StandardScaler()
    engagement_features = ['total_session_count', 'total_session_duration',
                          'match_start_count', 'win_rate', 'total_revenue']

    X = first_day_metrics[engagement_features].copy()
    X_scaled = scaler.fit_transform(X)

    kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
    first_day_metrics['engagement_segment'] = kmeans.fit_predict(X_scaled)

    segment_labels = {0: 'Low Engagement', 1: 'Medium Engagement', 2: 'High Engagement'}
    first_day_metrics['engagement_segment_label'] = first_day_metrics['engagement_segment'].map(segment_labels)

    # Basit bir görsel: segment dağılımı
    figures = {}
    fig, ax = plt.subplots(figsize=(10, 6))
    segment_counts = first_day_metrics['engagement_segment_label'].value_counts()
    colors = ['#ff6b6b', '#ffd93d', '#6bcf7f']
    ax.pie(segment_counts.values, labels=segment_counts.index, autopct='%1.1f%%',
           colors=colors, startangle=90)
    ax.set_title('First-Day Engagement Segment Distribution')
    figures['first_day_segment_distribution'] = fig

    return first_day_metrics, figures


def analyze_session_duration_trends(df):
    # Oyun süresi zaman içinde uzuyor mu kısalıyor mu? (En çok sorulan sorulardan biridir.)

    daily_stats = df.groupby('event_date').agg({
        'total_session_duration': 'sum',
        'total_session_count': 'sum',
        'user_id': 'nunique'
    }).reset_index()

    daily_stats['avg_session_duration'] = (
        daily_stats['total_session_duration'] /
        daily_stats['total_session_count'].replace(0, np.nan)
    )

    df_with_days = df.copy()
    df_with_days['days_since_install'] = (
        (df_with_days['event_date'] - df_with_days['install_date']).dt.days
    )

    duration_by_days = df_with_days.groupby('days_since_install').agg({
        'total_session_duration': 'sum',
        'total_session_count': 'sum',
        'user_id': 'nunique'
    }).reset_index()

    duration_by_days['avg_session_duration'] = (
        duration_by_days['total_session_duration'] /
        duration_by_days['total_session_count'].replace(0, np.nan)
    )

    # İlk 30 günü anlamak
    duration_by_days_30 = duration_by_days[duration_by_days['days_since_install'] <= 30].copy()

    valid_data = duration_by_days_30.dropna(subset=['avg_session_duration'])

    figures = {}

    # Zaman içinde ortalama session süresi
    fig, ax = plt.subplots(figsize=(14, 6))
    ax.plot(daily_stats['event_date'], daily_stats['avg_session_duration'],
            linewidth=2, color='#4a90e2')
    ax.set_title('Average Session Duration Trend Over Time')
    figures['session_duration_daily_trend'] = fig

    return daily_stats, duration_by_days, figures


def additional_creative_analyses(df):
    # Bu bölüm tamamen yaratıcılık alanı. Ek analizler koyuyoruz.

    figures = {}

    df['days_since_install'] = (df['event_date'] - df['install_date']).dt.days

    retention_by_day = df.groupby('days_since_install')['user_id'].nunique().reset_index()
    retention_by_day.columns = ['days_since_install', 'active_users']
    day0_users = df[df['days_since_install'] == 0]['user_id'].nunique()
    retention_by_day['retention_rate'] = (retention_by_day['active_users'] / day0_users * 100)

    # Basit retention grafiği
    retention_30 = retention_by_day[retention_by_day['days_since_install'] <= 30]
    fig, ax = plt.subplots(figsize=(14, 6))
    ax.plot(retention_30['days_since_install'], retention_30['retention_rate'], color='#e24a4a')
    ax.set_title('User Retention Over Time')
    ax.set_xlabel('Days Since Install')
    ax.set_ylabel('Retention Rate (%)')
    figures['user_retention'] = fig

    return figures


def save_visualizations(figures_dict):
    for name, fig in figures_dict.items():
        file_path = FIGURES_DIR / f"{name}.png"
        fig.savefig(file_path, dpi=300, bbox_inches='tight')
        plt.close(fig)


def main():
    print("User Characteristics Analysis - Task 2")

    try:
        df = load_data(DATA_DIR)
    except Exception as e:
        print(f"ERROR loading data: {e}")
        return

    all_figures = {}

    first_day_metrics, first_day_figures = analyze_first_day_engagement(df)
    all_figures.update(first_day_figures)

    daily_stats, duration_by_days, duration_figures = analyze_session_duration_trends(df)
    all_figures.update(duration_figures)

    creative_figures = additional_creative_analyses(df)
    all_figures.update(creative_figures)

    save_visualizations(all_figures)
    print(f"Analysis complete! Visualizations saved to: {FIGURES_DIR}")


if __name__ == "__main__":
    main()
