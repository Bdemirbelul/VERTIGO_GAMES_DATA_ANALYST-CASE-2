PS C:\Users\bdemi\source\repos\Vertigo_games_task2\Vertigo_games_task2> python analysis/main_analysis.py
==================================================
User Characteristics Analysis - Task 2
==================================================
Found 17 gzipped CSV files. Loading...
Loading file 1/17: 000000000000.csv.gz
Loading file 2/17: 000000000001.csv.gz
Loading file 3/17: 000000000002.csv.gz
Loading file 4/17: 000000000003.csv.gz
Loading file 5/17: 000000000004.csv.gz
Loading file 6/17: 000000000005.csv.gz
Loading file 7/17: 000000000006.csv.gz
Loading file 8/17: 000000000007.csv.gz
Loading file 9/17: 000000000008.csv.gz
Loading file 10/17: 000000000009.csv.gz
Loading file 11/17: 000000000010.csv.gz
Loading file 12/17: 000000000011.csv.gz
Loading file 13/17: 000000000012.csv.gz
Loading file 14/17: 000000000013.csv.gz
Loading file 15/17: 000000000014.csv.gz
Loading file 16/17: 000000000015.csv.gz
Loading file 17/17: 000000000016.csv.gz

Dataset loaded: 7,293,526 rows, 14 columns

Column names: ['user_id', 'event_date', 'platform', 'install_date', 'country', 'total_session_count', 'total_session_duration', 'match_start_count', 'match_end_count', 'victory_count', 'defeat_count', 'server_connection_error', 'iap_revenue', 'ad_revenue']

Data types:
user_id                            object
event_date                 datetime64[ns]
platform                           object
install_date               datetime64[ns]
country                            object
total_session_count                 int64
total_session_duration            float64
match_start_count                   int64
match_end_count                     int64
victory_count                       int64
defeat_count                        int64
server_connection_error             int64
iap_revenue                       float64
ad_revenue                        float64
dtype: object

Date range: 2024-02-15 00:00:00 to 2024-03-15 00:00:00

Unique users: 2,453,499

First few rows:
            user_id event_date  ... iap_revenue ad_revenue
0  C6C0A027C49B98BA 2024-02-16  ...         0.0        0.0
1  EE03D492BC0ED08C 2024-03-08  ...         0.0        0.0
2  5CAA4AF817354059 2024-03-12  ...         0.0        0.0
3  EF0DE79217D56E72 2024-02-16  ...         0.0        0.0
4  6DD3D1FC631486F0 2024-03-02  ...         0.0        0.0

[5 rows x 14 columns]

Basic statistics:
                          event_date  ...    ad_revenue
count                        7293526  ...  7.293526e+06
mean   2024-02-29 07:37:05.502345216  ...  2.006868e-02
min              2024-02-15 00:00:00  ...  0.000000e+00
25%              2024-02-22 00:00:00  ...  0.000000e+00
50%              2024-02-29 00:00:00  ...  0.000000e+00
75%              2024-03-08 00:00:00  ...  1.144138e-02
max              2024-03-15 00:00:00  ...  3.236633e+01
std                              NaN  ...  9.454978e-02

[8 rows x 11 columns]

Missing values:
user_id                        0
event_date                     0
platform                       0
install_date                   0
country                    17998
total_session_count            0
total_session_duration         0
match_start_count              0
match_end_count                0
victory_count                  0
defeat_count                   0
server_connection_error        0
iap_revenue                    0
ad_revenue                     0
dtype: int64

======================================================================

==================================================
ANALYSIS 1: First-Day Engagement Segmentation
==================================================

Users with first-day data: 1,056,852

First-day engagement statistics:
       total_session_count  ...  total_revenue
count         1.056852e+06  ...   1.056852e+06
mean          1.409627e+00  ...   4.349480e-02
std           8.099775e-01  ...   2.123261e+00
min           0.000000e+00  ...   0.000000e+00
25%           1.000000e+00  ...   0.000000e+00
50%           1.000000e+00  ...   0.000000e+00
75%           2.000000e+00  ...   4.483469e-03
max           1.800000e+01  ...   1.670070e+03

[8 rows x 4 columns]

Segment Statistics:
                         total_session_count         ... total_revenue user_id  
                                        mean median  ...           sum   count  
engagement_segment_label                             ...
High Engagement                         1.15    1.0  ...         78.94  216899  
Low Engagement                          1.22    1.0  ...      14245.63  711078  
Medium Engagement                       2.86    3.0  ...      31643.00  128875  

[3 rows x 10 columns]

======================================================================

==================================================
ANALYSIS 2: Session Duration Trends Over Time
==================================================

Daily average session duration statistics:
count      30.000000
mean     1064.110667
std        25.537794
min      1019.740486
25%      1042.492321
50%      1064.019536
75%      1088.256473
max      1115.390205
Name: avg_session_duration, dtype: float64

Average session duration trend (first 30 days):
   days_since_install  avg_session_duration
0                  -1            158.278000
1                   0            821.099766
2                   1            842.552450
3                   2            855.826436
4                   3            877.554296
5                   4            913.023593
6                   5            941.374653
7                   6            996.311224
8                   7           1023.911531
9                   8           1042.552703

Trend Analysis (first 30 days):
Slope: 13.8341 minutes per day
R-squared: 0.4880
P-value: 0.0000
Trend: Sessions are getting LONGER over time

======================================================================

==================================================
ANALYSIS 3: Additional Creative Analyses
==================================================

--- User Retention Analysis ---
Day 0 users: 1,056,852
Day 1 retention: 46.32%
Day 7 retention: 8.51%
Day 30 retention: 2.96%

--- Monetization Analysis ---
Total users: 2,453,499
Paying users: 35,089 (1.43%)
Ad viewers: 1,032,601 (42.09%)
Total IAP Revenue: $933,579.99
Total Ad Revenue: $146,371.47
Average Revenue per User (ARPU): $0.44
Average Revenue per Paying User (ARPPU): $27.20

--- Geographic Analysis ---
Top 10 countries by user count:
           country  unique_users  total_revenue
27          Brazil        225367   42963.924061
214        Türkiye        197153   71347.165141
170         Russia        181041   18138.612536
220  United States        176497  199588.542464
225        Vietnam        115575   23380.610694
95           India        109813   17005.662122
217        Ukraine         81744   23276.336632
96       Indonesia         65045   17301.418655
8        Argentina         58193    2743.254963
107     Kazakhstan         55021    6494.820581

--- Gameplay Behavior Analysis ---
Average win rate: 47.49%
Average match completion rate: 64.54%

--- User Lifetime Value Analysis ---
Average user lifetime: 5.8 days
Average lifetime value: $0.44
Median lifetime value: $0.00

==================================================
Saving visualizations...
==================================================
Saved visualization: C:\Users\bdemi\source\repos\Vertigo_games_task2\Vertigo_games_task2\outputs\figures\first_day_segment_distribution.png
Saved visualization: C:\Users\bdemi\source\repos\Vertigo_games_task2\Vertigo_games_task2\outputs\figures\first_day_metrics_comparison.png
Saved visualization: C:\Users\bdemi\source\repos\Vertigo_games_task2\Vertigo_games_task2\outputs\figures\first_day_revenue_analysis.png
Saved visualization: C:\Users\bdemi\source\repos\Vertigo_games_task2\Vertigo_games_task2\outputs\figures\session_duration_daily_trend.png
Saved visualization: C:\Users\bdemi\source\repos\Vertigo_games_task2\Vertigo_games_task2\outputs\figures\session_duration_by_days_since_install.png
Saved visualization: C:\Users\bdemi\source\repos\Vertigo_games_task2\Vertigo_games_task2\outputs\figures\session_duration_and_count_trends.png
Saved visualization: C:\Users\bdemi\source\repos\Vertigo_games_task2\Vertigo_games_task2\outputs\figures\session_duration_by_lifecycle.png
Saved visualization: C:\Users\bdemi\source\repos\Vertigo_games_task2\Vertigo_games_task2\outputs\figures\gameplay_behavior.png      

==================================================
Analysis Complete!
==================================================
✓ Visualizations saved to: C:\Users\bdemi\source\repos\Vertigo_games_task2\Vertigo_games_task2\outputs\figures
✓ Reports saved to: C:\Users\bdemi\source\repos\Vertigo_games_task2\Vertigo_games_task2\outputs\reports

Total visualizations created: 11