# FUND-114 — Original-language research source

> Mechanically extracted from the publisher PDF; not translated. See [source.pdf](source.pdf) for original layout and [metadata.json](metadata.json) for provenance.

## PDF page 1

1
Frontiers of Information T echnology & Electronic Engineering
www.jzus.zju.edu.cn; engineering.cae.cn; www.springerlink.com
ISSN 2095-9184 (print); ISSN 2095-9230 (online)
E-mail: jzus@zju.edu.cn
Supplementary materials for
Liyuan CHEN, Gaoguo JIA, Dongsheng GU, Jiangpeng YAN, Yuhang JIANG, Xiu LI, Xiaojun ZENG, 2025. MEN-
TOR: a multi-agent framework for event and narrative trend prediction with optimized reasoning. Front Inform
Technol Electron Eng, 26(10):1847-1861. https://doi.org/10.1631/FITEE.2500608
1 Evaluation for trending event detec-
tion
The following are the deﬁnitions and calculation
details of the evaluation metrics for trending event
detection:
ERR = N
mentions
Ntotal_posts
ICR = Nreporting_inﬂuencers
Ntotal_inﬂuencers
KPQ = Nkey_points
Ntotal_points
SDI = 1
N
N∑
i=1
(Xi − μ)2
⎫
⎪⎪⎪
⎪
⎪
⎪
⎪
⎪
⎪
⎪⎪⎪
⎪
⎪
⎪
⎪
⎪
⎪
⎬
⎪⎪
⎪⎪⎪
⎪
⎪
⎪
⎪
⎪
⎪
⎪⎪⎪
⎪
⎪
⎪
⎪
⎭
E = −
n∑
i=1
pi logb(pi)
(S1)
where Nmentions represents the number of times a
speciﬁc event is mentioned across all public accounts,
and N
total_posts denotes the total number of posts
published by all public accounts within the same
time frame. Nreporting_inﬂuencers represents the num-
ber of inﬂuential public accounts reporting on a spe-
ciﬁc event, and N
total_inﬂuencers denotes the total
number of inﬂuential public accounts. Nkey_points
represents the number of associated key points ex-
tracted from the text, and Ntotal_points denotes the
total number of key points in the text related to the
speciﬁc event. N represents the total number of key
points, X
i denotes the sentiment score of the i-th
key point, and μ is the mean sentiment score of all
key points. E represents the current entropy value,
which is derived from the computation of four heat
metrics.
2 Statistical signiﬁcance of perfor-
mance gains
We assess the signiﬁcance of MentorâĂŹs im-
provement over the strongest baseline (SEP_O1)
using the Wilcoxon signed-rank test on 30 boot-
strap samples of industry rankings (Spearman corre-
lation). Results are shown in Table S1.
T able S1 Wilcoxon test results ( n =3 0)
Market Statistic ( W ) p-value
A-share 29.0 3.24 × 10−6
S&P 500 122.0 0.022
Both improvements are statistically signiﬁcant
(p< 0.05). The much stronger signiﬁcance on A-
share is likely due to its broader time coverage and
larger sample size, which yield more stable estimates.
The statistic W is the smaller of the signed rank
sums; lower values indicate more consistent outper-
formance.
3 Prompt templates
We provide representative prompt templates
used in the MENTOR framework. For a given task,
multiple prompt templates may be utilized for two
primary reasons. First, some templates are deliber-
ately designed for ablation studies. Second, the out-
puts produced by certain prompts on speciﬁc models
may deviate from the required format speciﬁcations.
To enhance robustness and ensure compatibility, the
system is conﬁgured to sequentially attempt the cor-
responding prompt templates in a predeﬁned order.

## PDF page 2

2
3.1 Hot event summarization
Based on the following stock market-related hot
events, please summarize the top 10 hot events that
occurred, ranked by their impact on the stock mar-
ket: hot_events
3.2 Hot event prediction
Based on the following stock market-related hot
events from last week, predict the top 10 hot events
that will occur in the next week. Write in sum-
mary format rather than prediction format, ranked
by their impact on the stock market.
Last week events: last_week_events
Improvement guidance: solution
3.3 Improvement suggestions templates
T emplate 1: Original
The following are hot events that occurred in a
certain week: actual_events
Below is a previous prediction by a certain large
model for events that might occur in that week: pre-
diction
Please score this model’s prediction out of 10
points, adding one point for each correct prediction,
and provide potential improvement ideas. Do not
consider adding new quantitative models or data,
but rather correct wrong thinking patterns and pro-
vide correct thinking approaches to avoid overﬁtting
to single data instances. The ﬁnal improvement ideas
will become prompts for new models. Please enclose
them in square brackets [], with only one set of brack-
ets containing all prompts.
T emplate 2: Direct
Compare the predicted events with actual
events and provide improvement suggestions:
Actual events: actual_events
Predicted events: prediction
Please provide improvement suggestions for fu-
ture predictions. Format your ﬁnal suggestions as:
[your suggestions here]
T emplate 3: Simpliﬁed
Based on the prediction accuracy, provide im-
provement guidance for better future predictions.
Actual: actual_events
Predicted: prediction
Improvement suggestions: [insert suggestions
here]
T emplate 4: Analytical
Performance Analysis:
Expected outcomes: actual_events
Model predictions: prediction
Please analyze the diﬀerences and provide
methodology improvements. Format: [analytical
recommendations]
T emplate 5: Research feedback
Evaluation Summary:
Observed events: actual_events
Forecasted events: prediction
Assess accuracy and suggest enhancement
strategies. Use format: [strategy improvements]
3.4 Industry ranking prediction templates
T emplate 1: Direct hot_events
The above are market events related to mar-
ket_desc from a recent week. Below are the weekly
performance data of industry_count market_desc
industries: result_str
Based on this information, please analyze and
provide a ranking of industry performance for the
upcoming week. Output format: [’Industry1’, ’In-
dustry2’, ’Industry3’, ... ’Industryindustry_count’].
additional_prompt
T emplate 2: Analytical
Market Analysis Context:
Recent market developments: hot_events
Historical performance data for industry_count
market_desc industries: result_str
Task: Analyze the trends and provide a per-
formance ranking for next week’s market outlook.
Please list industries in order of expected perfor-
mance. Format: Python list with industry names.
additional_prompt
T emplate 3: Academic
Financial Market Research:
Market events summary: hot_events
Industry performance metrics for market_desc
market (industry_count sectors): result_str
Please conduct a trend analysis and suggest the
likely performance ranking for the following period.
Return as a list format: [’Sector1’, ’Sector2’, etc.].
additional_prompt
T emplate 4: Data-driven
Data Analysis Request:
Weekly market data for industry_count indus-
tries: result_str
Recent market context: hot_events

## PDF page 3

3
Based on the data patterns, please arrange the
industries in order of expected performance. Output:
list format.
additional_prompt
3.5 Ranking evaluation templates
T emplate 1: Professional Prediction Analysis:
Context: prediction_context
Predicted ranking: predicted_ranking
Actual performance data: actual_str
Please evaluate the prediction accuracy on a
scale of 1-10 and suggest methodological improve-
ments. Format suggestions as: [improvement ideas]
T emplate 2: Academic review
Research Evaluation:
Methodology context: prediction_context
Forecast results: predicted_ranking
Observed outcomes: actual_str
Provide an assessment score (1-10) and recom-
mendations for methodology enhancement. Enclose
recommendations in brackets: [suggestions]
T emplate 3: Analytical feedback
Performance Review:
Analysis background: prediction_context
Projected outcomes: predicted_ranking
Actual market results: actual_str
Rate the forecasting accuracy (1-10) and oﬀer
analytical improvements. Format: [enhancement
recommendations]
T emplate 4: Simple comparison
Comparison Analysis:
Prediction: predicted_ranking
Reality: actual_str
Context: prediction_context
Score the accuracy (1-10) and suggest better ap-
proaches. Use format: [improvement suggestions]
3.6 Extracting score templates
T emplate 1: Original
Please extract the prediction score given by the
large model from the following text. Extract the
total combined score, the score obtained in a ten-
point scale, do not include /10, only extract numbers,
enclose in[]: text
T emplate 2: Direct
Extract the numerical score (0-10) from this
text: text
Score: [your answer]
T emplate 3: Simple
What is the score mentioned in this text? For-
mat: [score]
Text: text
3.7 Updating solution with feedback tem-
plates
T emplate 1: Original
current_solution
The above is the original prompt (if any).
The following is a supplement to the original
prompt:feedback
Please generate a new prompt based on the sup-
plement. Format your response as: [new prompt
here]
T emplate 2: Direct
Current guidance: current_solution
New feedback: feedback
Please combine them into an improved guid-
ance. Provide your response as: [improved guidance]
T emplate 3: Simple
Improve this guidance: current_solution
Using this feedback: feedback
New guidance: [your response]
4 Data samples of Chinese KOL arti-
cles texts and English ﬁnancial news
texts
4.1 Data samples of Chinese KOL articles
texts
Overview
This part provides data samples of English news
texts, which contain copyrighted content licensed
from Reuters. Due to the licensing agreement, the
complete dataset cannot be made publicly available.
Data structure
The data is organized in a tabular format with
the following columns:
ID: A unique identiﬁer for each text entry.
TITLE: The title of the relevant content, indi-
cating the text’s topic.
AUTHOR: The name of the author or the or-
ganization behind the text.
CONTENT_TIME: The date and time that
the content was created.

## PDF page 4

4
URL: The Web link to the original content,
which has been partially masked for data pro-
tection.
CONTENT: The actual text content from
which potentially identifying information has
been removed.
Sample entries
Here is a sample entry demonstrating the above
- mentioned data structure:
ID: [Masked ID 1]
TITLE: Revival of Weimar by Baoneng Group,
Aiming for 120 Billion in 5 Years
AUTHOR: 21st Century Business Review
CONTENT_TIME: 2025 - 09 - 09 19:52:10
URL: [Masked URL 1]
CONTENT: Weimar Automobile is seeing a
revival opportunity. On September 6th, it and
Baoneng Automobile jointly issued a "White
Paper to Suppliers", stating that they are fully
promoting the resumption of mass production at
the Wenzhou base and ensuring the production
of over 10,000 EX5 and E.5 models by the end
of the year. The new shareholder, Xiangfei Au-
tomobile, which has close ties to Baoneng, plans
an initial investment of 1 billion yuan for factory
equipment upgrades, supply chain restoration,
and product development. It aims to produce
100,000 vehicles by 2026 with an expected rev-
enue of nearly 10 billion yuan, and challenges
a production target of 1 million vehicles and a
revenue of 120 billion yuan by 2030. However,
Weimar has debt issues. The ordinary credi-
tors of the four restructured Weimar companies
with claims of 150,000 yuan or less can receive
full - cash settlement within 6 months. Those
with larger claims can get 150,000 yuan in cash,
and the remaining amount will be included in
a trust for later proportional settlement. The
article also discusses the company’s production
plans, market situation, and recruitment eﬀorts.
4.2 Data samples of English ﬁnancial news
texts
Overview
This part provides data samples of English news
texts, which contain copyrighted content licensed
from Reuters. Due to the licensing agreement, the
complete dataset cannot be made publicly available.
Data structure
The data is presented in a tabular format with
the following columns:
md5_doc_id: A unique identiﬁer for each
news document in MD5 hash format.
headline: The title or headline of the news ar-
ticle, summarizing the main topic.
content: The full text content of the news
piece, with detailed reports related to the head-
line.
doc_url: The web link to the original news
document, which has been partially masked.
pub_code: A code associated with the publi-
cation.
source: The source of the news.
section: The section of the publication where
the news appears.
author: The author of the news article.
region: The region related to the news, provid-
ing geographical context.
Sample entries
Here is a sample entry demonstrating the above
- mentioned data structure:
md5_doc_id: [Masked ID 2]
headline: Carbon Credit Trading Platform
Market Estimation Worth $556.8 Million by
2032
content: Allied Market Research reveals that
the global carbon credit trading platform mar-
ket, valued at $112.4 million in 2022, is set for re-
markable growth. It’s projected to reach $556.8
million by 2032, growing at a CAGR of 17.4%
from 2023 to 2032. A carbon credit trading
platform serves as an online marketplace en-
abling the buying and selling of carbon cred-
its, which are rights to emit speciﬁc amounts of
greenhouse gases. This plays a crucial role in

## PDF page 5

5
helping businesses, governments, and organiza-
tions meet emissions reduction goals and con-
tribute to climate change mitigation.
doc_url: [Masked URL 2]
pub_code: [Masked pub_code 1]
source: [Masked source 1]
section: [Masked section 1]
author: [Masked author 1]
region: American
