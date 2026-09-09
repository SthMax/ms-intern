> 原语言机械提取；公式、图表以PDF原件为准。

## PDF page 1

LREC-COLING 2024, pages 773–783
20-25 May, 2024. © 2024 ELRA Language Resource Association: CC BY -NC 4.0
773
AlphaFin: Benchmarking Financial Analysis with Retrieval-
Augmented Stock-Chain Framework
Xiang Li1*, Zhenyu Li1*, Chen Shi2*,
Yong Xu1, Qing Du1†, Mingkui Tan1, Jun Huang2
1South China University of Technology, China
2Alibaba Group, China
{lixiangjacky, zhenyuli2148}@gmail.com, deling.sc@alibaba-inc.com
Abstract
The task of financial analysis primarily encompasses two key areas: stock trend prediction and the corresponding
financial question answering. Currently, machine learning and deep learning algorithms (ML&DL) have been widely
applied for stock trend predictions, leading to significant progress. However, these methods fail to provide reasons for
predictions, lacking interpretability and reasoning processes. Also, they can not integrate textual information such
as financial news or reports. Meanwhile, large language models (LLMs) have remarkable textual understanding
and generation ability. But due to the scarcity of financial training datasets and limited integration with real-time
knowledge, LLMs still suffer from hallucinations and are unable to keep up with the latest information. To tackle
these challenges, we first release AlphaFin datasets, combining traditional research datasets, real-time financial
data, and handwritten chain-of-thought (CoT) data. It has a positive impact on training LLMs for completing financial
analysis. We then use AlphaFin datasets to benchmark a state-of-the-art method, called Stock-Chain, for effectively
tackling the financial analysis task, which integrates retrieval-augmented generation (RAG) techniques. Extensive
experiments are conducted to demonstrate the effectiveness of our framework on financial analysis.
Keywords:Large Language Models, Retrieval-Augmented Generation, Chain-of-Thoughts, Finance, Stock
Trend Prediction, Financial Question Answering
1. Introduction
With the advancement of the financial industry, the
importance of financial analysis has become in-
creasingly prominent. The ability of financial anal-
ysis is primarily manifested in the areas of stock
trend prediction and the corresponding financial
Q&A. The advent of LLMs has attracted attention
from the financial industry, as they possess excep-
tional generation capabilities (Dredze et al., 2016;
Araci, 2019; Bao et al., 2021). Thus, there is a
strong desire to leverage these LLMs to enhance
the accuracy of financial analysis.1
Numerous recent studies have attempted to cre-
ateefficientalgorithmsusingML&DLforstocktrend
prediction (Saad et al., 1998; Shah et al., 2022). At
present, ML&DL has been widely used for stock
trend prediction based on time series data, gener-
ating a positive impact on the industry. However,
ML&DL algorithms have limited performance, only
able to provide uncertain results and incapable of
handling complex textual data. Meanwhile, they
fail to provide investors with effective justifications
and analyze the underlying causes, potentially dis-
* Equal contribution. This work was conducted when
Xiang Li and Zhenyu Li were interning at Alibaba.
† Corresponding author.
1Resources are publicly available at: https://
github.com/AlphaFin-proj/AlphaFin
Input : 
Input:Here is the latest report of Apple Inc., …{stock price: 170, 173,  … 192}. WhatisyouropiniononAppleInc.'sstockpricenextmonth?
Ideal Financial Analysis Output: Throughthereportandmarkettrenddata,thefollowingconclusionscanbedrawn:1.Fundamentals:in the 2023 fiscal year , Apple Inc. …2.Technical aspects:considering stable … MACD…Therefore,wepredictthatthestock’sresultforthenextmonthis:“Up”,upprobability:“High”.
Output :Up    ( 52% )  Down( 48%)Input :[172.40, 173.66, 174.91, 177.49, 178.99,178.39, … 179.80, 180.71 178.85, 178.62]ML&DL
LLMOutput (unhelpful):ThestockpriceofAppleInc.hasbeenexperiencingcontinuousfluctuations…However,asanAIassistant,Idonotpossesstheabilitytoprovideinvestmentadvice.
Figure 1: An example of the financial analysis task,
including stock trend prediction and financial Q&A.
Traditional ML&DL methods merely provide uncer-
tain forecasts (Up/Down) without any justification,
while original LLMs could offer analysis of the pre-
diction but unhelpful.
rupting their investment confidence. As shown in
Figure 1, for Apple Inc., ML&DL (such as LSTM)
can predict an uncertain stock trend (“up”) for the
next month based on the former stock price data.
Nevertheless, it could not provide a reliable result
and analysis of the prediction. If they could offer ef-
fective analysis, it would greatly enhance investor’s
confidence in decision-making.

## PDF page 2

774
Fortunately, LLMs possess excellent capabilities
in text processing and generation. To utilize the
capacity of LLMs, FinGPT (Yang et al., 2023b) and
BloombergGPT(Wuetal.,2023)havebeenspecifi-
cally designed as FinLLMs. They can be applied to
various financial tasks, catering to the needs of the
industry. AsshowninFigure1,theyhavethepoten-
tial to handle diverse text data, including news and
reports (Zhang et al., 2023). This advancement
empowers investors to make precise investment
and trading decisions.
Nevertheless, building a FinLLMs is not a
straightforward task. LLMs often exhibit phenom-
ena such as hallucination and meaningless out-
puts (Mündler et al., 2023), even for the advanced
ChatGPT (Ouyang et al., 2022). As shown in Fig-
ure 1, the content generated by general LLMs
lacks helpfulness and fails to meet real-time re-
quirements. This can be attributed to two reasons.
Firstly, the quality of generated content relies on
data availability. The absence of high-quality finan-
cial training datasets (Radford et al., 2019) impacts
thequalityofgeneration. Secondly, stocktrendpre-
diction relies on precise and real-time information,
the absence of these information leads to LLMs
hallucinations. Despite the widespread application
of RAG (Lewis et al., 2021) in other fields, their
adaptation in the financial domain remains insuffi-
cient.
To tackle these challenges, in this paper, we for-
malize the task of financial analysis and release
AlphaFinforfine-tuningFinLLMs, whichcontaintra-
ditional research datasets, real-time financial data,
andhandwrittenCoTdata. Moreover,weproposea
Stock-ChainframeworkintegratedwithRAG.Stock-
Chain not only provides investors with stock trend
prediction but also integrates real-time market data
and macroeconomic news through RAG, enabling
accurate stock analysis during interactions for in-
vestors.
Experimental results demonstrate that Stock-
Chain is able to achieve the task of stock trend
prediction with state-of-the-art accuracy and over
30% annualized rate of return (ARR). Meanwhile,
Stock-Chaincanprovidecomprehensiveanalysisin
the financial Q&A, enhancing investors’ confidence
in decision-making and providing a solid founda-
tion for their investment choices. We conduct ex-
tensive supplementary experiments like ablation
study, GPT4&human preference evaluation, and
case study.
In summary, the contribution lies in four folds:
• We formally define the task of financial analy-
sis, which aims to accomplish stock trend pre-
diction and the corresponding financial Q&A.
• WeproposeAlphaFindatasets,whichcontains
traditional research datasets, real-time finan-
EastmoneyWallStreetcnCCTVTushareYa h o oFinancialNewsDatasetTushareAKshareStockQADatasetDataY esFinancialReportDatasetManuallyCoTReport
ResearchDatasets
HeadlineFinQAFPB ChatGPT
ChatGPT
…
Figure 2: The data source and preprocessing of
the proposed AlphaFin datasets.
cial data, and handwritten CoT data, enhanc-
ing LLMs’s ability in financial analysis.
• We fine-tune a StockGPT based on AlphaFin
datasets and integrate it to a Stock-Chain
framework, which is further integrated with a
real-time financial database through RAG. By
integrating with RAG, we address the issue of
the hallucination of LLMs’s output and LLMs’s
inability to generate real-time content.
• We conduct extensive experiments on the Al-
phaFin datasets, to reveal that Stock-Chain
outperforms all the baseline methods, and
shows effectiveness for financial analysis.
2. AlphaFin Datasets
We release AlphaFin datasets, as shown in Fig-
ure 2, which include four parts, research datasets,
StockQA, financial news, and financial reports. Al-
phaFin is sourced from a dozen of data sources.
From Table 1, it is evident that the traditional re-
search dataset exhibits relatively shorter length
of label, which hampers the training of FinLLMs.
Thus, AlphaFin addresses the issue of low quality
and length in traditional research datasets. In this
section, we provide the details of its sources and
construction process.
2.1. Data Sources
• Research datasets: This part includes tradi-
tional financial datasets from the academic, in-
cluding FPB (Malo et al., 2014), FinQA (Maia
Dataset Size Input Label Type
Research 42,373 712.8 5.6 en
StockQA 21,000 1313.6 40.8 zh
Fin. News 79,000 497.8 64.2 zh
Fin. Reports 120,000 2203.0 17.2 zh
Fin. Reports CoT 200 2184.8 407.8 zh
Table 1: The details of the AlphaFin datasets. “In-
put” and “Label” denote their text length.

## PDF page 3

775
et al., 2018), convFinQA (Chen et al., 2022b)
and Headline (Sinha and Khandait, 2020), etc.
which enhance the information extraction and
summarization ability for LLMs.
• StockQA dataset: This part encompasses
stock price and other financial data from
Tushare (Tushare, 2021) and AKshare (AK-
share, 2021). It utilizes sequential data format,
such as the real-world stock price trend (e.g.
{..., 170, 173, 171, 175, 173, 170, ...}).
• Financial News dataset: To provide real-
world financial knowledge for LLMs, we incor-
porate online news sources, such as the finan-
cial sections of CCTV, and Wall Street CN.
• Financial reports dataset: We build finan-
cial report datasets via DataYes (DataYes,
2021), including professional analysis and
knowledge of companies conducted by finan-
cial institutions.
2.2. Data Preprocessing
As shown in Figure 2, we explore the details of
AlphaFin preprocessing:
• Research dataset : Traditional research
datasets are primarily in English and of sub-
stantialquantity. ToenhancetheLLMs’sability
in Chinese and ensure quality fine-tuning, we
only sample a portion from the source.
• StockQA dataset: Given the source data
is presented in sequential format, we utilize
ChatGPT with the following prompt, to gen-
erate financial questions upon it.Based on
the ..., give me a good financial
question. Input: <sequential
data>, Output: <Question>. This
can facilitate training and enhance the di-
versity of questions. Subsequently, we use
ChatGPT to generate responses and obtain
Q&A pairs for training LLMs.
• Financial News dataset: We leverage Chat-
GPT to extract a summary for each news, and
construct the financial news dataset. This pro-
cess improves LLMs’s ability to generate sum-
maries for financial news.
• Financial reports dataset : We manually
align the financial reports for the companies
and their stock price on the day of report
publication, and use the following template to
generate the final data.According to ...
give a clear answer up or down.
Input: <reports & stock price>,
Output: <Up/down>.
Furthermore, we manually create 200 financial
reports CoT data with professional financial
knowledge and longer labels, to provide the
LLMs with progressive analytical ability. The
output format is:
According to ... conclusions can
be drawn: 1. Fundamentals: ...
2. Technical aspects: ...
Therefore, we predict the ... is
<up/down>, probability: <Prob>
3. Stock-Chain Framework
We treat the financial analysis task as two counter-
parts, stock trend prediction and the corresponding
financial Q&A. Thus, our proposed Stock-Chain
framework is divided into two stages as shown in
Figure 3. In this section, we first formalize the task,
and then introduce the details of both two stages.
3.1. Problem Definition
For the first stage, given a set of companiesC =
{ci}N
i=1 and the corresponding knowledge docu-
ments D = {dj}M
j=1 , we can predict stock trends:
P redi = ϕ(ci, dj), P red i ∈ {up, down} (1)
where ϕ represents a stock predicting system, and
dj is retrieved as the related documents for com-
pany ci. The goal is to choose a subset of compa-
nies Cchosen that are predicted to rise.
Cchosen = {ci|ci ∈ C ∧ P redi = up} (2)
For the second stage, we treat a multi-turn di-
alogue session as a sequence of several query-
response pairs between two interlocutors. We
denote Qt and Rt as the user query and agent
response at the current time stept, and Ht =
[Q0, R0, ..., Qt−1, Rt−1] as the dialogue history.
Then we formalize the financial Q&A task as ob-
taining the response based on the current query,
dialogue history, and corresponding documents:
Rt = π(dk, Ht, Qt) (3)
where π represents the conversation system, and
dk is the retrieved document related toQt.
3.2. Stage-1: Stock Trend Prediction
AsshownintheleftpartofFigure3,ourfirststageis
stock trend prediction. Given a companyci and the
corresponding documentdj, this stage maintains a
stock predicting systemϕ by combining LLMs and
AlphaFindatasets,togivethestocktrendprediction
P redi for ci.
3.2.1. Knowledge Processing
As shown in Figure 31⁄bigcircle, given a companyci, we
first retrieve the related documentsdj for it. Then,
we design a prompt templateP rompt1 as follows:

## PDF page 4

776
Stage2Retrieval-AugmentedQ&A
+
UserQuery
Ve c t o rDBa1q1
AlphaFinDatasetsFin.NewsStockQA
Research
LoRAFine-Tuning
DailyUpdate
Construct
Prompt2
1
2
3
4q2s1…a2d1…
DocumentsInput
RetrieveResponse
Stage1StockTrendPrediction
Extract
LoRAFine-Tuni ng
AlphaFinDatasetsFin.Reports Fin. CoTReportsPrompt1Please predict the rise and fall of AppleIncin next month based on …X
H
Pretrained weights B ="
#=$(",'!)
Document_1[Report]AppleInc‘s Q1performance outperforming the industry and the promotion of the ...
+StockGPTstage1Input
AccumulatedReturn
1
2
3
StockPrediction
✅UpDownDocument_2[StockPrice]{‘2023-03-01’: 7.94,‘2023-02’: 7.96... }
𝜙 𝜋
Retrieve
Response…Therefore, the result of this stock for next month is: ‘Down’.
StockGPTstage1
StockGPTstage2
Figure 3: An illustration of the Stock-Chain framework of the two stages in financial analysis.
Please predict the rise and fall
of the stock next month based on
the research reports and data pro-
vided below. Please provide a clear
answer, either “up" or “down". <re-
port><market data>
where <report> and <market data> com-
pose dj. Ultimately, we concatenate the prompt
with the documents to get the inputIi to the LLMs.
Ii = concat(P rompt1, dj) (4)
3.2.2. StockGPT Fine-Tuning
As shown in Figure 32⁄bigcircle, we design the fine-tuning
process of an LLM, called StockGPT, which in-
cludes two steps. Firstly, we leverage all the fi-
nancial report datasets of AlphaFin for training. In
the second step, we utilize the manually created
report CoT dataset to guide the model to think step-
by-step. All fine-tuning processes for StockGPT
utilize the Low-Rank Adaptation (LoRA) (Hu et al.,
2021) method.
Through the fine-tuning of the two steps, we ob-
tain StockGP Tstage1, which is able to predict the
trend ofci based ondj more accurately, as well as
providing detailed analysis and explanations.
3.2.3. Prediction and Post-process
As shown in Figure 33⁄bigcircle, given the InputIi, we
leverage StockGPT to predict the rise and fall of
the stock, which can be viewed as a binary classifi-
cation task. By feedingStockGP Tstage1 the input
Ii, we obtain the response textResi about ci.
The format ofResi could be referred to as Sec
2.2. The <Prob> is a category in the range of:
{very large, large, medium to upper, average },
which could be a piece of supplementary informa-
tion for the investor’s decision-making.
Resi = StockGP Tstage1(Ii) (5)
Then, we manually extract the prediction result
P redi from Resi. Finally, we choose all stocks pre-
dicted as “up” asCchosen.
P redi =

up, if “up” ∈ Resi
down, else (6)
Cchosen = {ci|P redi = “up”} (7)
Additionally, we implement this investment strat-
egy rolling by months. Every month, for all theci in
Cchosen, we hold them throughout the month. The
proportion of each stock in the portfolio is calcu-
lated via a capitalization-weighted approach.
ARm = ARm−1 +
X
ci∈Cchosen
w ∗ Rci (8)
where ARm is the accumulated return of month
m, and Rci is the return of stockci. w denotes
the proportion of stockci in the portfolio.vi is the
market value of companyci.
w = vi
PN
n=1 vn
(9)
3.3. Stage-2: Financial Q&A
Besides stock trend prediction, the proposed Stock-
Chain also has the ability for financial Q&A, which
could be more constructive for investors.
Given a dialogue historyHt, user queryQt, and
the retrieved documentdj related toQt, conversa-
tion systemπ can give a responseRt. We adopt
RAGtoenhancetheQ&AabilityofLLMs,whichtyp-
ically includes three parts: vector DB construction,
knowledge retrieval, and response generation.
3.3.1. Vector DB Construction
As shown in Figure 3 stage 21⁄bigcircle, vector DB is an
important part of RAG, which is used for efficient
storage and retrieval of knowledge documents.

## PDF page 5

777
Knowledge Extraction To improve the accu-
racy and efficiency of document retrieval, we
extract the key knowledge from the document.
We adopt two extraction strategies: coarse-
grained document-level summarizing with Chat-
GPT, and fine-grained entity-level dialogue gen-
eration through RefGPT (Yang et al., 2023a). For
document dk, the extraction process for the two
strategies is as follows:
sk = ChatGP T (dk) (10)
(qk0, ak0), (qk1, ak1), ... = Ref GP T(dk) (11)
where sk denotes the summary ofdk, and(qk_, ak_)
is query-answer pair of the generated dialogues.
Forexample,for dk aboutkline, qk_ couldbe“What
is the meaning of k line?".
Knowledge Embedding We take the extraction
strategy of ChatGPT as an example. Given sum-
mary sk, we obtain the embedding vectoresk via a
sentence embedding model. This vector would be
stored in the database for subsequent retrieval.
esk = SentEmbed (sk) (12)
where SentEmbed isasentenceembeddingmodel,
such as BGE (Xiao et al., 2023) and SGPT (Muen-
nighoff, 2022). We adopt BGE as the embedding
model in our framework.
Continuous Updating Finally, we construct a
vector DB including reports, market data, and fi-
nancial news. The knowledge documents in the
DB could be continuously updated via online data
backflow, to keep the knowledge in real time.
3.3.2. Knowledge Retrieval
To retrieve knowledge in the vector DB, user query
Q would also be fed into the same sentence em-
bedding model to obtain the embedding vectoreQ.
eQ = SentEmbed (Q) (13)
Wechoosethedocumentwiththehighestcosine
similarity to the query as the external knowledge
aided StockGPT in generating responses.
d∗ = arg max
dk
e⊤
Q · esk
|eQ||esk | (14)
where sk and dk could be replaced byqk_ and ak_
for the extraction strategy of RefGPT.
3.3.3. LLMs Fine-Tuning
We inherit StockGP Tstage1 as the base LLMs in
this part, then continue trainingStockGP Tstage1 on
the research dataset, financial news, and StockQA
datasets of AlphaFin to obtainStockGP Tstage2.
3.3.4. Response Generation
Given a dialogue historyHt, user queryQt, and
retrieved documentd∗ related toQt, the goal is to
give the responseRt in a conversation of turnt.
We provide a prompt templateP rompt2 as follows:
You are an intelligent assistant,
please answer my question. To help
you ... local knowledge base is pro-
vided as follows: <knowledge>
Now, answer the question...: <his-
tory><query>
Then, we concatenate the prompt template, re-
trieved knowledge, conversation history, and user
query to get the inputIt for LLMs. FeedingIt into
StockGPT, we can get the responseRt.
It = concat(P rompt2, d∗, Ht, Qt) (15)
Rt = StockGP Tstage2(It) (16)
4. Experiments
In this section, we conduct experiments to validate
Stock-Chain’sabilitytoaccomplishthetaskoffinan-
cialanalysis. Duetothestructureofourframework,
experiments can be divided into two parts. The
experiments in the first part mainly examine the
model’s annualized rate of return and accuracy. In
the second part, we demonstrate the performance
of our Stock-Chain via preference evaluation with
human&GPT-4, ablation study, and case study.
4.1. AlphaFin-Test Datasets
We select a subset of data from the data sources,
whichisexcludedfromthetrainingdataset,toserve
as our test dataset. Given that all the research
datasets are in English, our main focus is on sam-
pling from other datasets. Such as financial reports
and StockQA datasets. For stage 1, we choose
the test datasets from the financial report dataset.
An example demonstration is as follows:Accord-
ing to ..., please judge the trend
of the company and give a clear an-
swer up or down. Input: <reports &
stock price>, Output: <Up/down>. As
for stage 2, the test dataset is sampled from the
StockQAandresearchdatasets. TheAlphaFin-test
datasets allow us to evaluate the model’s ability in
the capital market.
4.2. Baselines
To fully validate the effectiveness of our Stock-
Chain on the test dataset, we select four categories
of models:
• Major Indices: We select indices in the Chi-
nese capital market, including the SCI, CSI
300, SSE50, and CNX.

## PDF page 6

778
Figure 4: Accumulated returns (AR) of each baseline under the test set of the financial report dataset
from January 2020 to July 2023. The figure shows the curves of some baselines.
Model ARR ↑ AERR ↑ ANVOL ↓ SR ↑ MD ↓ CR ↑ MDD ↓ ACC ↑
SSE50 -1.0% -2.7% 19.3% -0.054 45.9% -0.023 29 -
CSI 300 1.7% 0 18.2% 0.092 39.5% 0.043 30 -
SCI 3.9% 2.2% 14.8% 0.266 21.5% 0.183 19 -
CNX 7.6% 5.9% 26.5% 0.287 41.3% 0.185 20 -
Randomforest 9.8% 8.1% 19.5% 0.501 16% 0.608 22 55.5%
RNN 8.1% 6.4% 10.9% 0.742 15.7% 0.515 12 54.1%
BERT 10.7% 9.0% 16.1% 0.664 13.5% 0.852 14 51.4%
GRU 11.2% 9.5% 13.7% 0.814 14.6% 0.765 21 54.7%
LSTM 11.8% 10.1% 15.4% 0.767 15.3% 0.768 19 55.2%
Logistic 12.5% 10.8% 27.1% 0.463 32.5% 0.385 18 54.8%
XGBoost 13.1% 11.4% 20.5% 0.633 20.9% 0.619 17 55.9%
Decision Tree 13.4% 11.7% 19.6% 0.683 11.9% 1.126 20 55.1%
ChatGLM2 8.1% 6.4% 24.9% 0.324 62.6% 0.126 26 49.5%
ChatGPT(3.5Turbo) 14.3% 12.6% 27.7% 0.516 53.6% 0.267 23 51.4%
FinMa 15.7% 14.0% 37.1% 0.422 66.3% 0.236 25 49.1%
FinGPT 17.5% 15.8% 28.9% 0.605 55.5% 0.312 24 50.5%
Stock-Chain 30.8% 29.1% 19.6% 1.573 13.3% 2.314 10 55.7%
Table 2: The main experimental results on AlphaFin-Test. ARR (Annualized rate of return) and ACC
(Accuracy rate) are core indicators, while the middle indicators (like AERR, ANVOL, etc.) could assist
investors in evaluating the model’s effectiveness. Since the rate of return usually fluctuates wildly, to
ensure the stability of the performance, we run each model 10 times and obtain the average result.
• ML&DL Algorithms: We employ ML algo-
rithms such as Logistic and XGBoost, and DL
models like LSTM and GRU, which are widely
employed for time-series prediction.
• General LLMs: We focus on the general-
purpose LLMs like ChatGLM2 and ChatGPT.
These LLMs have been chosen due to their
ability and wide range of applications in NLP.
• FinLLMs: In the financial domain, we focus
on open-source FinLLM, such as FinGPT and
FinMA, which have been trained for financial
tasks like financial analysis and forecasting.
4.3. Settings
For stage 1, the experiments aim to predict the
trend of stock price for the next month and observe
the model’s returns in the real market.
• ML&DL: Due to their limitations, they can only
analyze time series data. Thus, their inputs
are restricted to the stock prices.
• LLMs: In contrast, LLMs possess generative
abilities, allowing them to incorporate both the
report data and the stock price series data.
For stage 2, we examine the model generation
capability and use GPT4&human as the evaluator.

## PDF page 7

779
All LLMs’ generation strategies are greedy search
to achieve optimal and stable performance and
integrated RAG in our experiments.
Among them, the hyperparameters are as fol-
lows: batch size 16, LoRA rank 8, cosine lr sched-
uler, learning rate 5e-5, bf16, and 1 NVIDIA A800-
80GB for all training processes. Specifically, in
stage 1, we trained 4 epochs for the first step and
20 epochs for the second step. In stage 2, we
used StockGP Tstage1 as the base model, and in-
crementalfine-tuneditfor2epochsontheAlphaFin
dataset.
4.4. Metrics
For stage 1, we utilize two categories of indicators.
The first category is core indicators, including ARR
and ACC, which gauge profitability. The second
category is supplementary indicators that assist
in analyzing different models, such as maximum
drawdown (MD), Calmar Ratio (CR), and Sharpe
ratio (SR), which measure risk assessment. With
these indicators, we have a thorough evaluation of
the model’s capabilities. For stage 2, we use the
ROUGE (Chin-Yew, 2004) as an evaluation metric,
which is used to measure the similarity between
the generated output and reference information.
Also, we use GPT4&human as the referee for scor-
ing. By considering these indicators, we can better
evaluate the performance of the models.
Model ARR ↑ SR ↑ Out_len ↑ N/A ↓
ChatGLM2 8.1% 0.324 228.1 52.3%
w/ raw_data 15.8% 0.636 17.2 -
w/ CoT_data 10.1% 0.469 476.1 32.4%
Stock-Chain 30.8% 1.573 254.8 25.9%
Table 3: The ablation results for stage 1 under
different training data. Out_len: average length of
LLMs outputs. N/A: invalid answer ratio.
Model ROUGE-1 ↑ROUGE-2 ↑ROUGE-L ↑
ChatGLM2 0.2794 0.1944 0.2642
w/ Fin. News 0.3477 0.2821 0.3445
w/ Fin. reports 0.2611 0.1603 0.2396
Stock-Chain 0.4352 0.3056 0.4031
Table 4: The ablation results for stage 2 under
different training data.
4.5. Comparison Results
As shown in Figure 4, the curve represents the
AR of each method. It is noteworthy that Stock-
Chain achieves the highest AR and maintains an
upward trend, starting from 2023. It indicates the
effectiveness of Stock-Chain in investment.
By referring to Table 2, Stock-Chain achieves
the highest 30.8% of ARR demonstrating its effec-
tiveness. Based on Table 2, we can derive the
following observations:
Firstly, ML&DL possesses certain analytical abil-
ities in stock trend prediction, they achieve impres-
sive ARR. Secondly, after integrating report data
with market data, LLMs generally surpass ML&DL,
leading to an enhancement in stock trend predic-
tion abilities. ChatGPT achieves an ARR of 14.3%.
While LLMs are trained on vast amounts of textual
data, they lack optimization for financial domains.
Thus, by fine-tuning for financial domains, FinLLMs
can improve stock trend prediction ability. The Fin-
GPT model achieves an ARR of 17.5%.
Finally, after fine-tuning Stock-Chain based on
financial report cot data, we achieve an ARR of
30.8% and an ACC of 55.63%. AlphaFin datasets
play a crucial role in the training of LLMs. By uti-
lizing comprehensive financial data for fine-tuning,
we improve prediction accuracy and return, thus
validating the performance of Stock-Chain.
53%57%60%85%
25%24%25%14%
22%19%15%1%
0%25%50%75%100%ChatGPTFinGPTChatGLMFinMa
Ours WinTieOurs Lose
Figure 5: Preference evaluations via human.
58%72%73%95%
6%2%3%4%
36%26%24%1%
0%25%50%75%100%ChatGPTFinGPTChatGLMFinMa
Ours WinTieOurs Lose
Figure 6: Preference evaluations via GPT-4.
4.6. Ablation Study
We conduct two ablation experiments. Firstly, we
observe the stock trend prediction ability of our
Stock-Chain by analyzing the effects of fine-tuning
atdifferentdata. BasedonTable3,comparedtothe
ChatGLM2, the ability of the LLMs to predict stock
price has shown improvement after fine-tuning with

## PDF page 8

780
How is the recent financial report of Apple Inc.? Is it worth investing?
1.【Reports】Inthefirstthreequartersof2023,Apple Inc.,achievedanoperatingincome…2.【MarketData】Stockprices:{‘2023-10-02’: 172.40…‘2023-10-12’: 180.71,…}Knowledge
Throughtheresearchreportandmarkettrenddata,thefollowingconclusionscanbedrawn:1.Fundamentals:In the 2023 fiscal year (April 2022 to March 2023), Apple Inc., achieved a total revenue of …the adjusted EBITDA exceeded …2.Technical aspect:ConsideringApple Inc.’s stable growth in recent years and its leading position in the logistics industry,…At the same time, the MACD index appeared dead cross…Therefore,wepredictthatthestock’sfinalreturnresultforthenextmonthis:“up”,upprobability:“average”
As an AI language model, I am unableto provideany recent reports or investment suggestions regarding Apple Inc. My knowledge is limited to the general information in the pre trained model. For issues related to investment and financial decision-making, it is recommended to consult professional financial advisors or reliable financial media.
Stock-Chain
ChatGPT
Retrieval
As an AI language model, according to the recent market data of AppleInc.you provided, Icannot predictthe rise and fall of the stock. The rise and fall prediction needs to take into account a variety of factors, such as market sentiment, macroeconomic conditions, company fundamentals, etc., which are difficult to predict accurately in the short term. …To sum up, I cannot give an exact answer to the rise and fall forecast of AppleInc.However, investors can make analysis and judgment based on factors such as market conditions, industry and company fundamentals.I'm sorry, Ican't answer this question because I'm a computer program and I don't have access to external data or information. You can refer to market expectations and the views of other investors to make investment decisions.
FinGPT
FinMA
Figure 7: Case of outputs of Stock-Chain, FinGPT, FinMA, and ChatGPT
raw and CoT data, achieving returns of 15.8% and
10.1% respectively.
Additionally, the proportion of invalid answers
also improved. It is worth mentioning that after
fine-tuning with the raw data, the LLMs’s output
only includes rise and fall, thus resolving the is-
sue of invalid answers. After fine-tuning with two
sets of data, our Stock-Chain achieves optimal per-
formance with 30.8% ARR, and the proportion of
invalid answers also decreased, reaching 25.9%.
As for the second ablation experiment, we inves-
tigate whether the quality of the output improved
after fine-tuning the LLMs at different data.
Based on Table 4, we observe that the scores of
Stock-Chain in terms of rouge1 and rouge2 reach
0.3477 and 0.2821 respectively after fine-tuning
with News data. Furthermore, it is noteworthy that
Stock-Chain achieves optimal performance after
fine-tuning with both news and reports.
4.7. Preference Evaluation
We employ GPT-4 and humans as the judge to rate
the output performance of each LLM on the test
datasets. All LLMs have integrated RAG in this
experiment. In the human section, Stock-Chain
outperforms other LLMs in terms of content effec-
tiveness. Based on Figure 5, compared to Chat-
GLM2, Stock-Chain achieves a win rate of over
60%, and when compared to FinLLMs, such as Fin-
GPT,thewinratereaches62%. BasedonFigure6,
when GPT4 is the judge, similar conclusions were
drawn. Stock-Chainexhibitshigherratescompared
to human ratings, with a win rate of 58% against
ChatGPT and 73% against ChatGLM2. Overall,
Stock-Chain’s output is effective.
4.8. Case Study
We present partial outputs of Stock-Chain for quali-
tative analysis. As shown in Figure 7, when users
inquire about recent reports and investment ad-
vice related to Appe Inc., Stock-Chain acquires
real-timerelevantinformationandmarketdatafrom
the knowledge base and provides them as input
to the LLMs. The output of the LLMs has been
enhanced, and the news remains up-to-date, en-
abling investors to analyze and receive recommen-
dations. However, as for ChatGPT and FinGPT,
we observe that it has great defects in the quality
and real-time response. Thus, by integrating RAG,
Stock-Chain addresses the issues of hallucinations
andinsufficientreal-timeoutputsinLLM,enhancing
the LLMs’s practicality and ability.

## PDF page 9

781
5. Related Work
5.1. Financial Datasets
General financial datasets include a wealth of in-
formation derived from various sources within the
financial industry, such as Internet data and pro-
prietary data. Currently, the main financial dataset
sets include a variety of tasks. FPB (Malo et al.,
2014) and FiQA-SA (Maia et al., 2018) are mainly
used for emotion analysis. The Headline (Sinha
and Khandait, 2021) dataset is primarily utilized
for news headline identification. For question
answering, we primarily utilize the FinQA (Chen
et al., 2022a) and ConvFinQA (Chen et al., 2022b)
datasets. Regrettably, the finance domain still suf-
fers from a scarcity of text datasets, impeding the
development of FinLLMs. To bridge this gap, we
propose AlphaFin, providing support for the finan-
cial industry in training its own FinLLMs.
5.2. Algorithms in Financial Domain
Traditional ML&DL algorithms, such as LSTM (Yu
et al., 2019), Logistic (Sperandei, 2014), and
BERT (Devlin et al., 2018), have been applied
in stock trend prediction. However, ML&DL fo-
cuses on the final result, without analyzing the un-
derlying factors driving market trend. As for Fin-
LLMs, although BloombergGPT (Wu et al., 2023),
FinMA (Xie et al., 2023), and FinGPT (Yang et al.,
2023b) play important roles in the community, they
are mainly based on English-language datasets. In
contrast, Stock-Chain relies on Chinese-language
and is specifically designed for stock trend predic-
tion.
As for RAG, it has attracted growing attention
in the community (Li et al., 2022). Compared to
the traditional method, RAG has remarkable per-
formance in various NLP tasks (Cai et al., 2021;
Weston et al., 2018). However, without RAG, Fin-
LLMs often produce hallucinations and meaning-
less outputs. Thus, we integrate LLMs with RAG
to address the above issues.
6. Conclusion
In this work, we formalize the task of financial
analysis, and propose AlphaFin datasets to en-
hance LLMs’s ability, and fine-tune the StockGPT
upon it. Then we propose the Stock-Chain frame-
work that integrates a real-time financial database
through RAG, to address the issue of hallucination
of LLMs’s output and LLMs’s inability to generate
real-time content. We conduct extensive experi-
ments on the proposed AlphaFin datasets, as well
as some supplementary experiments like ablation
study, GPT4&human preference evaluation and
case study, to reveal that Stock-Chain outperforms
all the baseline methods, and shows effectiveness
for the task of financial analysis.
7. Ethical considerations and
limitations
We assert that there are no ethical dilemmas sur-
rounding the submission of this article and have
no known competing financial interests or personal
relationships that could have had an impact on the
research work presented.
Despite the positive contributions of this study,
we recognize that there is still great room for de-
velopment in our work. In our future work, we will
further contribute to the open-source FinLLMs, im-
prove its generalization, enhance its ability in other
financial tasks, and create a more powerful open-
source FinLLMs.
8. Bibliographical References
AKshare. 2021. Akshare - a financial online docu-
mentation.
Dogu Araci. 2019. Finbert: Financial sentiment
analysiswithpre-trainedlanguagemodels. arXiv
preprint arXiv:1908.10063.
Siqi Bao, Huang He, Fan Wang, Hua Wu, Haifeng
Wang,WenquanWu,ZhihuaWu,ZhenGuo,Hua
Lu, Xinxian Huang, et al. 2021. Plato-xl: Ex-
ploring the large-scale pre-training of dialogue
generation. arXiv preprint arXiv:2109.09519.
Deng Cai, Yan Wang, Huayang Li, Wai Lam, and
Lemao Liu. 2021. Neural machine translation
with monolingual translation memory. arXiv
preprint arXiv:2105.11269.
Zhiyu Chen, Wenhu Chen, Charese Smiley,
Sameena Shah, Iana Borova, Dylan Lang-
don, Reema Moussa, Matt Beane, Ting-Hao
Huang, Bryan Routledge, and William Yang
Wang. 2022a. Finqa: A dataset of numerical
reasoning over financial data.
Zhiyu Chen, Shiyang Li, Charese Smiley, Zhiqiang
Ma, Sameena Shah, and William Yang Wang.
2022b. Convfinqa: Exploring the chain of numer-
ical reasoning in conversational finance question
answering. arXiv preprint arXiv:2210.03849.
Lin Chin-Yew. 2004. Rouge: A package for auto-
maticevaluationofsummaries. In Proceedings of
the Workshop on T ext Summarization Branches
Out, 2004.
DataYes. 2021. Datayes - financial data and ana-
lytics platform.

## PDF page 10

782
Jacob Devlin, Ming-Wei Chang, Kenton Lee, and
Kristina Toutanova. 2018. Bert: Pre-training of
deep bidirectional transformers for language un-
derstanding. arXiv preprint arXiv:1810.04805.
Mark Dredze, Prabhanjan Kambadur, Gary Kazant-
sev, Gideon Mann, and Miles Osborne. 2016.
How twitter is changing the nature of financial
news discovery. Inproceedings of the second in-
ternational workshop on data science for macro-
modeling, pages 1–5.
Edward J Hu, Yelong Shen, Phillip Wallis, Zeyuan
Allen-Zhu, Yuanzhi Li, Shean Wang, Lu Wang,
and Weizhu Chen. 2021. Lora: Low-rank adap-
tation of large language models.arXiv preprint
arXiv:2106.09685.
Patrick Lewis, Ethan Perez, Aleksandra Piktus,
FabioPetroni, VladimirKarpukhin, NamanGoyal,
Heinrich Küttler, Mike Lewis, Wen tau Yih, Tim
Rocktäschel, Sebastian Riedel, and Douwe
Kiela. 2021. Retrieval-augmented generation
for knowledge-intensive nlp tasks.
Huayang Li, Yixuan Su, Deng Cai, Yan Wang,
and Lemao Liu. 2022. A survey on retrieval-
augmented text generation. arXiv preprint
arXiv:2202.01110.
Macedo Maia, Siegfried Handschuh, André Freitas,
Brian Davis, Ross McDermott, Manel Zarrouk,
and Alexandra Balahur. 2018. Www’18 open
challenge: financial opinion mining and question
answering. InCompanion proceedings of the the
web conference 2018, pages 1941–1942.
Pekka Malo, Ankur Sinha, Pekka Korhonen, Jyrki
Wallenius, and Pyry Takala. 2014. Good debt
or bad debt: Detecting semantic orientations in
economic texts. Journal of the Association for
Information Science and T echnology, 65(4):782–
796.
Niklas Muennighoff. 2022. Sgpt: Gpt sentence
embeddings for semantic search.
Niels Mündler, Jingxuan He, Slobodan Jenko, and
Martin Vechev. 2023. Self-contradictory hal-
lucinations of large language models: Evalu-
ation, detection and mitigation. arXiv preprint
arXiv:2305.15852.
LongOuyang,JeffreyWu,XuJiang,DiogoAlmeida,
Carroll Wainwright, Pamela Mishkin, Chong
Zhang, Sandhini Agarwal, Katarina Slama, Alex
Ray, et al. 2022. Training language models to
follow instructions with human feedback. Ad-
vances in Neural Information Processing Sys-
tems, 35:27730–27744.
Alec Radford, Jeffrey Wu, Rewon Child, David
Luan, Dario Amodei, Ilya Sutskever, et al. 2019.
Language models are unsupervised multitask
learners. OpenAI blog, 1(8):9.
Emad W Saad, Danil V Prokhorov, and Donald C
Wunsch. 1998. Comparative study of stock trend
prediction using time delay, recurrent and prob-
abilistic neural networks.IEEE T ransactions on
neural networks, 9(6):1456–1470.
Jaimin Shah, Darsh Vaidya, and Manan Shah.
2022. A comprehensive review on multiple hy-
brid deep learning approaches for stock predic-
tion. Intelligent Systems with Applications, page
200111.
Ankur Sinha and Tanmay Khandait. 2020. Impact
of news on the commodity market: Dataset and
results.
Ankur Sinha and Tanmay Khandait. 2021. Impact
of news on the commodity market: Dataset and
results. In Advances in Information and Commu-
nication: Proceedings of the 2021 Future of Infor-
mation and Communication Conference (FICC),
Volume 2, pages 589–601. Springer.
SandroSperandei.2014. Understandinglogisticre-
gression analysis. Biochemia medica, 24(1):12–
18.
Tushare. 2021. Tushare - a financial data interface.
JasonWeston,EmilyDinan,andAlexanderHMiller.
2018. Retrieve and refine: Improved sequence
generation models for dialogue.arXiv preprint
arXiv:1808.04776.
Shijie Wu, Ozan Irsoy, Steven Lu, Vadim Dabravol-
ski, Mark Dredze, Sebastian Gehrmann, Prab-
hanjan Kambadur, David Rosenberg, and
Gideon Mann. 2023. Bloomberggpt: A large
language model for finance. arXiv preprint
arXiv:2303.17564.
Shitao Xiao, Zheng Liu, Peitian Zhang, and Niklas
Muennighoff. 2023. C-pack: Packaged re-
sources to advance general chinese embedding.
Qianqian Xie, Weiguang Han, Xiao Zhang,
Yanzhao Lai, Min Peng, Alejandro Lopez-Lira,
and Jimin Huang. 2023. Pixiu: A large language
model, instruction data and evaluation bench-
mark for finance.
Dongjie Yang, Ruifeng Yuan, Yuantao Fan, , Yifei
Yang, Zili Wang, and Shusen Wang. 2023a.
Refgpt: Reference-to-dialogue by gpt and for
gpt. https://github.com/ziliwangnlp/
RefGPT.

## PDF page 11

783
Hongyang Yang, Xiao-Yang Liu, and Christina Dan
Wang. 2023b. Fingpt: Open-source finan-
cial large language models. arXiv preprint
arXiv:2306.06031.
YongYu,XiaoshengSi,ChanghuaHu,andJianxun
Zhang. 2019. A review of recurrent neural net-
works: Lstm cells and network architectures.
Neural computation, 31(7):1235–1270.
Boyu Zhang, Hongyang Yang, and Xiao-Yang
Liu. 2023. Instruct-fingpt: Financial senti-
ment analysis by instruction tuning of general-
purpose large language models.arXiv preprint
arXiv:2306.12659.
