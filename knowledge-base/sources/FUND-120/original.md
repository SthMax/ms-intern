# The Label Horizon Paradox: Rethinking Supervision Targets in Financial Forecasting

> Original-language PDF extraction. [PDF](source.pdf); [metadata](metadata.json). No translation; page numbers below are physical PDF pages.

## PDF page 1

The Label Horizon Paradox: Rethinking Supervision Targets in Financial
Forecasting
Chen-Hui Song 1 Shuoling Liu 1† Liyuan Chen 1†
Abstract
While deep learning has revolutionized financial
forecasting through sophisticated architectures,
the design of the supervision signal itself is rarely
scrutinized. We challenge the canonical assump-
tion that training labels must strictly mirror in-
ference targets, uncovering theLabel Horizon
Paradox: the optimal supervision signal often
deviates from the prediction goal, shifting across
intermediate horizons governed by market dynam-
ics. We theoretically ground this phenomenon in
a dynamic signal-noise trade-off, demonstrating
that generalization hinges on the competition be-
tween marginal signal realization and noise ac-
cumulation. To operationalize this insight, we
propose a bi-level optimization framework that
autonomously identifies the optimal proxy label
within a single training run. Extensive experi-
ments on large-scale financial datasets demon-
strate consistent improvements over conventional
baselines, thereby opening new avenues forlabel-
centricresearch in financial forecasting.
1. Introduction
Deep learning has fundamentally transformed the land-
scape of quantitative finance, serving as a critical tool for
high-noise time-series forecasting, particularly in short-term
stock prediction (Al-Khasawneh et al., 2025; Chen et al.,
2025; Sonkavde et al., 2023; Shah et al., 2022). The primary
objective in this domain is to forecast the relative returns
of assets to construct profitable portfolios. Unlike typical
tasks in computer vision or natural language processing, fi-
nancial prediction operates in an environment characterized
by extremely low signal-to-noise ratios and non-stationary
†Project Lead 1E Fund Management Co., Ltd., Guangzhou,
Guangdong, China. Correspondence to: Chen-Hui Song
<songchenhui@efunds.com.cn>, Shuoling Liu <liushuol-
ing@efunds.com.cn>, Liyuan Chen<chenly@efunds.com.cn>.
Proceedings of the 43 rd International Conference on Machine
Learning, Seoul, South Korea. PMLR 306, 2026. Copyright 2026
by the author(s).
dynamics. To tackle these intrinsic challenges, the research
community has traditionally divided its efforts into two
main streams:Data-centricapproaches (Shi et al., 2025;
Yu et al., 2023; Sawhney et al., 2020), which focus on engi-
neering expressive alpha factors from limit order books and
alternative data; andModel-centricapproaches (Liu et al.,
2024a; Wang et al., 2025; Liu et al., 2025; Chen & Wang,
2025), which design sophisticated architectures—ranging
from RNNs to Transformers—to capture complex temporal
dependencies.
However, this extensive focus on input representations and
model architectures has left a critical component largely
unexamined: the prediction target (or label) itself. In the
standard paradigm, the training label is strictly aligned with
the inference goal. For instance, in a daily prediction task
(where predictions are made at time t for the horizon t+ ∆ ,
with ∆ = 1 day), it is typically taken for granted that the
model must be trained on realized next-day returns. This
convention implicitly assumes that bringing the supervision
signal closer to the evaluation target is always beneficial,
rarely questioning the optimality of the label’s time horizon.
This raises a fundamental question:Is the “correct” infer-
ence target necessarily the best training signal?In this
paper, we answer this in the negative. Through extensive
experiments, we uncover a counter-intuitive phenomenon
we term theLabel Horizon Paradox:
Minimizing training error on the canonical target horizon
t+ ∆ does not guarantee optimal generalization on t+ ∆ .
Contrary to intuition, the most effective supervision signal
is oftenmisalignedwith the inference target, residing at
an intermediate horizon t+δ (where δ̸= ∆ ) that better
balances signal realization against noise.
Underlying this paradox is a fundamental trade-off gov-
erned by the temporal evolution of market information. We
conceptualize generalization performance not as a static
property, but as the outcome of a dynamic interplay between
two competing rates:
1. Marginal Signal Realization (Information Gain):In-
formation (Alpha) requires time to be absorbed by the mar-
ket and fully priced in (Hong & Stein, 1999; Shleifer, 2000).
1
arXiv:2602.03395v5  [cs.LG]  19 Aug 2026

## PDF page 2

The Label Horizon Paradox: Rethinking Supervision Targets in Financial Forecasting
2. Marginal Noise Accumulation (Noise Penalty):Simul-
taneously, as the time window expands, the market accu-
mulates idiosyncratic volatility and stochastic shocks (Ang
et al., 2006; Jiang et al., 2009) unrelated to the initial signal.
The generalization behavior is therefore governed by the in-
terplay between these two rates. Extending the label horizon
is beneficial only when marginal signal realization outpaces
noise accumulation. Conversely, once the signal is largely
priced in, the diminishing information gain is overwhelmed
by compounding noise, rendering further extension detri-
mental. The optimal horizon δ∗ therefore emerges at the
precise equilibrium where marginal information gain equals
the marginal noise penalty.
Crucially, since the underlying rates of signal realization and
noise accumulation are unknown and dynamic, the optimal
horizon δ∗ cannot be hard-coded a priori. To operationalize
this insight, we apply a Bi-level Optimization Framework
(Chen et al., 2022; Franceschi et al., 2018) for adaptive hori-
zon learning. Instead of manually selecting a fixed proxy,
our method treats the label horizon as a learnable param-
eter. By formulating the problem as a bi-level objective,
the model automatically learns to weight different horizons,
dynamically discovering the sweet spot where this trade-off
is maximized for the specific dataset and model architecture.
In this work, we focus on short-term stock forecasting and
make the following primary contributions:
1. Theoretical Unification:Grounded in Arbitrage Pric-
ing Theory, we provide a rigorous derivation using a linear
factor model to quantify the temporal dynamics of signal
realization and noise accumulation. This theoretical founda-
tion unifies previously fragmented empirical observations,
formally establishing the signal-noise trade-off as the pri-
mary driver of model generalization in financial forecasting.
2. Methodological Innovation:Motivated by our theo-
retical insights, we propose a novel, end-to-end adaptive
framework. By formulating temporal-horizon selection as a
dynamic optimization problem, our method automatically
identifies the optimal supervision signal in a single training
run, eliminating the need for the computationally prohibitive
brute-force search required by traditional methods.
3. Empirical Validation:We extensively evaluate our
framework across ten diverse architectures. Our approach
consistently yields significant predictive improvements in
the emerging A-share market (CSI 300, 500, and 1000)
and demonstrates robust cross-market generalizability in
the highly efficient US equity market (S&P 500). Further-
more, downstream backtesting and severe macroeconomic
stress testing (e.g., on the 2024 market crash) confirm its
exceptional resilience and practical profitability.
2. Preliminaries
In this section, we formalize the short-term stock cross-
sectional prediction task (Linnainmaa & Roberts, 2018) and
outline the deep learning framework employed.
2.1. Stock Cross-Sectional Prediction
Consider a universe of N stocks at a decision time t. Our
goal is to forecast the relative performance of these assets
over a subsequent fixed period, denoted as the target hori-
zon ∆ (where ∆ represents the number of time steps in
minutes). Let pi,t denote the price of stock i at time t.
The target variable, the target realized return, is defined as
r∆
i,t =p i,t+∆/pi,t −1.
We denote the simultaneous returns of the entire market as
a cross-sectional vectorr ∆
t = [r∆
1,t, . . . , r∆
N,t]⊤ ∈R N .
2.2. Optimization Objective
In quantitative investment, the primary goal is to construct
a portfolio that maximizes risk-adjusted returns. This ob-
jective is theoretically grounded in the Fundamental Law
of Active Management (Grinold & Kahn, 2000), which re-
lates the expected Information Ratio (IR) of a strategy to its
predictive power:
E[IR]≈IC·
√
Breadth.(1)
Intuitively, this law asserts that performance is driven by
the quality of predictions and the number of independent
trading opportunities. Specifically, Breadth represents the
number of independent bets (proportional to the universe
size N), and IC (Information Coefficient) is the Pearson
correlation coefficient ρ between the predicted scores and
the realized return vectorr ∆
t .
Since market breadth is generally fixed for a given strat-
egy, maximizing portfolio performance is mathematically
equivalent to maximizing the IC. Consequently, our learning
objective is to train a model that produces scores maximally
correlated with the target return r∆
t . In the sequel, we use
ICandρinterchangeably to denote this correlation.
2.3. Deep Learning Framework
Modern deep learning approaches capture market dynamics
by modeling stock features as time series. For each stock i
at time t, the input is a sequence of historical feature vectors
xi,t ∈R L×D, spanning a lookback window of size L with
D feature channels. Aggregating across the universe, the in-
put at time t forms a 3-dimensional tensor Xt ∈R N×L×D .
A deep neural network fθ (e.g., LSTM, GRU, or Trans-
former) encodes this history into a predictive score:
ˆyt =f θ(Xt)∈R N .(2)
2

## PDF page 3

The Label Horizon Paradox: Rethinking Supervision Targets in Financial Forecasting
…
…
…
…
𝑟𝑡𝛿 𝑟𝑡∆𝑟𝑡1
𝑋𝑡 𝑓𝜃
𝛿
𝑡𝑟𝑎𝑖𝑛
𝑖𝑛𝑓𝑒𝑟
𝑖𝑛𝑝𝑢𝑡
Figure 1.Training and Inference Pipeline.The leftmost panel shows historical input features Xt, which are processed by a neural
network model f δ
θ . The right panel illustrates unfolding future price paths with different time horizons (r1
t , rδ
t , r∆
t ). The arrows highlight
a central premise of this study: during training (top arrow), the model may be optimized against an intermediate proxy label rδ
t ; however,
during inference (bottom arrow), the model’s performance is strictly evaluated on its ability to forecast the final target return (r∆
t ). Our
goal is not to change the evaluation target, but to question and improve the choice of training label that best serves this fixed objective.
Standard financial forecasting paradigms rigidly align the
supervision label with the final inference goal. Typically,
models are trained to minimize a loss L(θ) =P
t ℓ(ˆyt,y t)
where the label yt is set strictly to the target return r∆
t . This
convention implicitly assumes that the target horizon pro-
vides the most effective learning signal, thereby defaulting
to the label horizon that conceptually matches the evaluation
metric.
However, relying solely on the terminal snapshot at t+ ∆
ignores the continuous price discovery process leading up to
that point. To investigate whether the trajectory offers better
supervision, we introduce a granular notation for interme-
diate dynamics. Let δ∈ {1, . . . ,∆} denote the discretized
time index within the prediction window. We definepi,t+δ
as the price of stock i at step δ. Consequently, the cumula-
tive return from decision time t to this intermediate horizon
is formulated asr δ
i,t =p i,t+δ/pi,t −1.
Aggregating these across the universe yields the interme-
diate return vector rδ
t ∈R N . In this work, we challenge
the dogma that the optimal supervision signal must mir-
ror the inference target (i.e., δ= ∆ ). Instead, we explore
how utilizing these proxy vectors rδ
t as training labels can
effectively enhance generalization on the final targetr∆
t .
3. The Label Horizon Paradox
Contrary to the standard practice of strictly aligning training
labels with prediction targets, the aforementioned Label
Horizon Paradox reveals the limitations of this convention.
This section presents empirical evidence of this phenomenon
and introduces a theoretical mechanism to explain it.
3.1. Empirical Observation
To systematically evaluate the impact of label horizon on
forecasting performance, we conducted a control experi-
ment as illustrated in Figure 1. While our ultimate inference
goal remains fixed—forecasting stocks based on the realized
return r∆ at the target horizon—we vary the supervision
signal used during training. Specifically, we train a set of
identical deep neural networks {f(δ)
θ }δ, where each model
is supervised by the cumulative return rδ
t at a specific inter-
mediate horizon δ∈ {1, . . . ,∆} . For clarity, we instantiate
this analysis using an LSTM backbone on the CSI 500 uni-
verse, as this mid-cap index offers a representative balance
between liquidity and cross-sectional breadth, and LSTMs
remain a strong and widely used baseline in short-term stock
forecasting. Detailed experimental settings are provided in
the Appendix A.
We examine this phenomenon across three distinct market
scenarios, which represent different prediction horizons in
quantitative finance:
Scenario 1: Interday (Standard) Prediction.The decision
time t is the market close on dayD, and the prediction target
r∆
t is the return from the close of day D to the close of day
D+ 1 . Intermediate horizons correspond to cross-sectional
returns at each minute of the next day. This setup follows
the standard convention in stock forecasting studies.
Scenario 2: Intraday (30-minute) Prediction.The de-
cision time t is set to the exact midpoint of the daily trad-
ing session. The target horizon is a short-term interval of
∆ = 30 minutes immediately following this timestamp. The
objective is to predict the return realized exclusively within
this 30-minute window.
Scenario 3: Intraday (90-minute) Prediction.Similarly,
the decision time t is fixed at the midpoint of the trading
session. The target horizon extends to∆ = 90 minutes. The
model aims to forecast the cumulative return realized over
this longer intraday interval within the same session.
We define the optimal training horizon as δ∗ =
argmaxδ ρ(ˆyδ
t ,r ∆
t ). As shown in Figure 2, the performance
curves exhibit distinct patterns across these scenarios:
3

## PDF page 4

The Label Horizon Paradox: Rethinking Supervision Targets in Financial Forecasting
0 50 100 150 200
0.075
0.080
0.085
0.090
0.095
0.100
0.105
(a)Scenario 1:δ ∗ ≪∆
0 10 20 30
0.133
0.135
0.138
0.140
0.143
0.145
0.148
0.150 (b)Scenario 2:δ ∗ ≈∆
0 20 40 60 80
0.090
0.095
0.100
0.105
0.110 (c)Scenario 3:0< δ ∗ <∆
Figure 2.Performance Curves across Different Scenarios.The x-axis is the training horizon δ, and the y-axis is the out-of-sample IC
on the fixed final targetr∆. The curves are obtained by training LSTM models on the CSI 500 dataset, with 5 independent models per
horizon. The blue line shows the raw results, and the red line shows the Gaussian-smoothed trend.
In Scenario 1, we observe aMonotonic Decrease. Perfor-
mance peaks at a very early horizon (δ∗ ≪∆ ) and degrades
significantly as δ approaches ∆. This strictly violates the
closer-is-better intuition.
In Scenario 2, we observe aMonotonic Increase. Here,
training on the target itself is optimal (δ∗ ≈∆ ). The signal
realization dominates the noise accumulation, meaning the
information gain continues until the target time. Conse-
quently, training on the target itself is optimal.
In Scenario 3, the curve is typicallyHump-Shaped. The
optimal horizon lies at an intermediate point (0< δ ∗ <∆ ).
This reflects an intraday trade-off: the model benefits from
alpha realization but suffers when forced to fit unpredictable
late-session noise.
These observations collectively confirm the Label Horizon
Paradox:Supervising the model with the exact target might
yield suboptimal generalization
3.2. Theoretical Framework
To provide a rigorous mechanism for the observations above,
we analyze the problem through a Linear Factor Model
grounded inArbitragePricingTheory (Reinganum, 1981),
hereafter referred to as APT. The details of our theoretical
analysis are provided in Appendix C.
We begin by modeling the intrinsic dynamics of market
returns.
Assumption 3.1.We extend the static APT framework to
model the short-term cumulative returnrδ
i,t using observable
factor exposuress i,t ∈R d:
rδ
i,t =α(δ)w ∗⊤si,t +ϵ δ
i,t, ϵ δ
i,t ∼ N(0, σ 2(δ+δ 0))(3)
Here, w∗ denotes the factor risk premia vector (i.e., the
ground-truth weight vector that linearly maps factor expo-
sures to expected returns), α(δ) represents the signal re-
alization process (i.e., how much of the information has
been priced in by horizon δ), and σ2 denotes the rate of
unpredictable noise accumulation.
Under this generative process, a model trained on the proxy
horizon δ yields an estimator ˆwδ corrupted by the specific
noise variance at that horizon. We define the generalization
performance J(δ) :=ρ 2(ˆyδ
t ,r ∆
t ) as the squared predictive
correlation with the fixed target r∆
t . By decomposing the
log-performance, we reveal the structural trade-off driving
the paradox:
Theorem 3.2.The expected performance is determined by
the net balance of two competing accumulation processes
(ignoring a constant term):
lnJ(δ) = 2 lnα(δ)| {z }
Information Gain
−ln

α(δ)2 +K(δ+δ 0)

| {z }
Noise Penalty
(4)
where K is a constant related to the model’s estimation
variance.
Equation (4) quantifies the fundamental tension in labeling:
1. Information Gainreflects the growth of valid signal in
the label. It increases as δ extends, but naturally saturates
asα(δ)→const(when information is fully priced).
2. Noise Penaltyreflects the growth of prediction uncer-
tainty. Since the idiosyncratic variance K(δ+δ 0) follows a
random walk, this penalty grows strictly with timeδ.
Consequently, the optimal horizon δ∗ defines the tipping
point where the marginal accumulation of noise begins to
outpace the marginal accumulation of information.
3.3. Generalization to Deep Learning
While Theorem 3.2 is derived for a linear estimator, its im-
plications can be intuitively related to deep neural networks.
From a representation-learning viewpoint, a deep model is
often viewed as a non-linear feature extractor followed by
a simple linear readout layer (Bengio et al., 2013; Alain
4

## PDF page 5

The Label Horizon Paradox: Rethinking Supervision Targets in Financial Forecasting
0 50 100 150 200
0.055
0.060
0.065
0.070
(a)Dataset CSI 300
0 50 100 150 200
0.080
0.085
0.090
0.095
0.100
0.105
0.110 (b)Dataset CSI 500
0 50 100 150 200
0.120
0.125
0.130
0.135
0.140
0.145 (c)Dataset CSI 1000
Figure 3.Decomposition Validation.The x-axis represents the training horizon δ, and the y-axis represents the Out-of-Sample IC on
the fixed final target r∆. We performed a dense experimental sweep to rigorously verify the theoretical decomposition, training distinct
LSTM models for every minute-level horizon across 5 random seeds. The red lines depict the empirical Test IC on the inference target
(∆), while the blue lines illustrate the theoretical values derived from the product term in Corollary 3.3. For both metrics, lighter shades
correspond to raw measurements from individual trials, while solid darker curves indicate the Gaussian-smoothed trends.
& Bengio, 2016). The latent representation learned by the
network can be thought of as playing the same role as the
signal si,t in our framework, and the final linear layer then
fits this signal under label noise, in line with standard lin-
ear or kernel-based generalization analyses (Belkin et al.,
2019; Jacot et al., 2018). Under this perspective, a simi-
lar trade-off is expected to influence deep models as well:
regardless of the complexity of the feature extractor, gener-
alization is shaped by the balance between realized signal
and accumulated noise in the supervision.
To empirically validate this theoretical connection, we
specifically examine Scenario 1. Given the interday na-
ture of this task, the market has ample time to absorb the
prior day’s information, causing the signal embedded in the
input features to be priced in immediately upon the market
open. Consequently, the signal realization saturates almost
immediately (α(δ)≈const ). This leads to the following
approximation:
Corollary 3.3.Under the condition where signal evolution
is static relative to noise accumulation, the final predic-
tive correlation can be approximated as the product of two
observable terms:
ρ(ˆyδ
t ,r ∆
t )≈ρ( ˆyδ
t ,r δ
t)×ρ(r δ
t ,r ∆
t )(5)
The detailed proof is provided in Appendix C.6.
We substantiate this corollary through large-scale experi-
ments, as shown in Figure 3. Notably, the theoretical curve,
calculated solely from the product on the right-hand side of
Eq. (5), closely matches the actual performance with high
precision across all datasets. This strong alignment con-
firms that the proposed signal-noise mechanism is indeed
the driving force in deep learning models.
Remark3.4.This decomposition can also be understood
from a purely statistical perspective via the Partial Correla-
tion Formula (Kenett et al., 2015). We discuss this alterna-
tive derivation in Appendix D, which further corroborates
the robustness of our theory.
3.4. Mechanism Analysis
Leveraging the signal-noise decomposition, we can now
interpret the distinct performance patterns observed across
the three scenarios:
Scenario 1 (Interday):Interday signals typically saturate
early (e.g., at the market open). Extending δ beyond this
point yields vanishing information gain (α′ ≈0 ) while the
noise penalty continues to grow linearly. Thus, the gradient
is strictly negative, driving the optimal horizon to be much
smaller than the target (δ∗ ≪∆).
Scenario 2 (30-min):In short, high-momentum windows,
the market is in a state of active price discovery. The sig-
nal realization rate remains high enough to suppress the
accumulation of noise. Consequently, the gradient remains
positive, making the full horizon optimal (δ∗ ≈∆).
Scenario 3 (90-min):Here, the signal’s effective lifespan
is shorter than the target window. Initially, rapid informa-
tion gain improves performance; however, once the signal
saturates, the persistent noise penalty eventually dominates,
resulting in a peak at an intermediate horizon (0< δ ∗ <∆ ).
A detailed mathematical discussion, categorizing these
regimes based on the sign of the derivative dlnJ(δ)/dδ ,
is provided in Appendix C.5.
4. Adaptive Horizon Learning via Bi-Level
Optimization
Since the theoretically optimal horizon is dynamic and a
brute-force search is expensive, we propose an automated
Bi-level Optimization (BLO) framework. This method au-
tonomously learns the ideal supervision during training,
5

## PDF page 6

The Label Horizon Paradox: Rethinking Supervision Targets in Financial Forecasting
stabilized by a warm-up phase and entropy regularization.
4.1. Bi-Level Optimization Framework
Our objective is to train a model fθ using a set of candidate
labels such that it generalizes best on the ultimate target
horizon ∆. We introduce a learnable weight vector λ∈
R∆ (obtained by applying a softmax to learnable logits, soP λδ = 1 ) to govern the importance of each candidate
horizon δ. We treat λ as learnable parameters and optimize
them via an intra-batch splitting strategy. In each iteration,
a mini-batch B is split into a support set Bin and a query set
Bout.
1. Inner Loop (Proxy Learning on Bin).The model
parameters θ are updated on Bin with loss function ℓ. The
final objective Linner is a weighted combination of losses
against the candidate return labelsR t ={r (δ)
t }δ:
Linner(θ,λ) =
X
(Xt,Rt)∈Bin
∆X
δ=1
λδ ·ℓ(f θ(Xt),r δ
t)(6)
Here, the model is guided by the composite signal empha-
sized byλ.
2. Outer Loop (Target Validation on Bout).The quality
of the learned weights λ is verified on Bout. Crucially, the
outer loss consists of the validation error against the target
Horizonr ∆
t and an entropy regularization term:
min
λ
Louter(θ∗(λ),B out)−γH(λ)(7)
s.t.θ ∗(λ) = arg min
θ
Linner(θ,λ,B in)(8)
whereH(λ) =−
X
δ
λδ logλ δ (9)
Louter =
X
(Xt,r∆
t )∈Bout
ℓ(fθ∗(Xt),r ∆
t )(10)
The added entropy term H(λ) acts as a safeguard against
noise disturbance. It prevents the weight distribution from
collapsing onto a single horizon—a scenario where tran-
sient noise artifacts could disproportionately dominate the
gradient and lead to training instability. Instead, it maintains
a smoother distribution, encouraging the model to leverage
complementary information from multiple horizons.
4.2. Optimization Procedure
Solving the bi-level objective requires differentiating
through the optimization path. We employ a two-phase
strategy to ensure stability.
Phase 1: Warm-up with Standardized Mean-Field.Ini-
tiating the bi-level optimization directly from scratch is
suboptimal, as the model parameters θ initially lack effec-
tive feature representations, making the meta-optimization
landscape highly volatile and prone to training collapse.
To address this, we employ a warm-up phase using stan-
dard supervised learning. We construct a robust supervision
signal by aggregating information across all horizons. How-
ever, since raw returns exhibit varying volatilities (scales),
we first apply cross-sectional standardization to narrow the
distributional gaps between different labels:
zδ
t = rδ
t −µ δ
t
σδ
t
(11)
For the firstNwarm epochs, the model is trained to minimize
a single loss function ℓ against the arithmetic mean of these
standardized candidates:
¯yt = 1
∆
∆X
δ=1
zδ
t (12)
This mean-field initialization efficiently establishes a foun-
dational representation, ensuring a stable starting point for
the subsequent bi-level adaptation.
Phase 2: Bi-Level Update.After warm-up, we enable the
adaptive weighting scheme. Given a batch split (Bin,B out):
1. Inner Loop Update.We simulate the learning trajectory
by performing M steps of gradient descent on Bin. Start-
ing from the current parameters θ, the model is updated
sequentially (m= 1, . . . , M):
θm(λ)←θ m−1 −η∇ θLinner(θm−1,λ)(13)
By retaining the computational graph of these updates, we
derive the look-ahead state θM(λ), which is functionally
dependent onλ.
Crucially, since the model has already acquired a robust
representation during the warm-up phase, a single gradient
step (M= 1 ) is typically sufficient to capture the sensitivity
of the parameters to the weights. This makes the process
highly computationally efficient.
2. Outer Loop Update.We evaluate θM on Bout against
the target r∆
t . We compute the gradient of the validation
loss w.r.t.λ, add the entropy gradient, and updateλ:
λ←λ−β∇ λ (Louter(θM ,λ)−γH(λ))(14)
By iterating these steps, λ converges to a robust distribution
that emphasizes the most effective horizons for supervision
signal extraction, with δ∗ = argmax δ λδ. Based on the
selected optimal horizon, we then retrain the forecasting
model using this horizon as the supervision target.
5. Experiments
In this section, we validate our proposed bi-level method
through extensive experiments on real-world market data. A
demo based on the open-source Alpha158 factors is also pro-
vided at https://github.com/Chenhui-Song/
label-horizon-paradox.
6

## PDF page 7

The Label Horizon Paradox: Rethinking Supervision Targets in Financial Forecasting
Table 1.Main Results.Comprehensive performance comparison between standard training (Std.) and our Bi-level framework (Ours)
across three market indices. All results are averaged over 5 random seeds. Bold indicates the better performance.
IC (×10) ICIR RANKIC (×10) RANKICIR TOPRET(%) SHARPERATIO
DATASETMODELSTD. OURSSTD. OURSSTD. OURSSTD. OURSSTD. OURSSTD. OURS
CSI 300
LSTM 0.6370.7200.4430.5620.6690.7270.5200.5560.2310.2402.3322.390
GRU 0.5860.7300.4450.5600.5660.6620.4360.5420.2090.2561.9402.612
DLINEAR0.5370.6840.4030.4050.5680.6830.4250.5160.2070.2212.0072.456
RLINEAR0.5650.7160.4240.5320.6250.6620.4610.5340.2110.2732.1392.781
PATCHTST 0.5680.6730.4110.4590.5250.6530.4110.4640.2130.2362.0782.381
ITRANSFORMER0.5400.6440.4130.4210.5600.6500.4280.4960.2160.2302.1962.518
MAMBA0.6410.7190.4570.5390.6460.6730.4620.5140.2380.2732.2712.570
BI-MAMBA+ 0.6610.7170.4850.4860.6310.7040.5240.5430.2450.2672.6982.956
MODERNTCN 0.5650.6860.3940.4230.5710.6940.4480.5480.2180.2272.3902.498
TCN 0.6040.6910.4590.4980.6320.7020.5030.5200.2160.2302.1022.240
CSI 500
LSTM 0.8451.0290.7240.8610.7920.8590.8610.8950.3820.3833.5343.660
GRU 0.8621.0790.7520.8860.8120.8830.8460.9390.3590.3823.3983.458
DLINEAR0.8390.9860.6320.7060.7870.871 0.8160.790 0.3200.3633.2193.495
RLINEAR0.7990.9610.6820.7500.7310.8390.7990.8150.3410.3663.1043.349
PATCHTST 0.9411.0700.8050.8730.7850.8610.8400.8550.3600.3953.1043.519
ITRANSFORMER0.8901.0040.7170.8100.7450.8580.8200.8770.3710.3773.3463.541
MAMBA0.9171.1410.8550.9080.7921.0060.8340.9330.3840.4053.4523.854
BI-MAMBA+ 0.9751.0810.8130.8760.8500.9280.9260.9430.3930.4263.7443.967
MODERNTCN 0.8821.0280.7930.8110.6400.8580.7830.8860.3540.3813.0963.554
TCN 0.8351.0140.7900.8290.7940.9070.7910.8720.3720.3833.3523.525
CSI 1000
LSTM 1.2751.3721.3111.3250.8070.8930.8420.8830.4940.5023.8884.050
GRU 1.3211.4101.2831.3970.8620.8890.8360.9710.4980.5254.1924.272
DLINEAR1.1071.2041.0211.2230.6350.7960.6200.9380.4460.4773.4504.067
RLINEAR1.0911.2071.0671.1830.7300.8270.8270.9210.4450.4803.4233.872
PATCHTST 1.2901.3891.3101.3490.7960.8710.8510.9260.4690.5023.6854.016
ITRANSFORMER1.2161.2961.2531.3520.6920.8750.7370.9950.4510.4743.4813.955
MAMBA1.3281.3761.2921.3310.8660.8730.9060.9070.4920.5103.9664.134
BI-MAMBA+ 1.3371.3771.2271.2840.7230.9270.7090.9680.4680.5103.6224.409
MODERNTCN 1.2131.3111.1921.2250.6540.9510.7230.8610.4770.4883.9554.143
TCN 1.0721.2190.9531.1270.8370.9020.9030.9090.4910.5114.1484.407
5.1. Experimental Setup
Data and Splitting.We evaluate our method on large-scale
real-world market data covering three major stock indices:
CSI 300 (Large-cap), CSI 500 (Mid-cap), and CSI 1000
(Small-cap). This selection ensures the evaluation covers
diverse market dynamics across different market capitaliza-
tions. The dataset spans from January 2019 to July 2025.
To strictly prevent look-ahead bias, we employ a chronolog-
ical split: Training (Jan 2019 – July 2023), Validation (July
2023 – July 2024), and Testing (July 2024 – July 2025).
Additional datasets for evaluation on the US S&P 500 and
historical stress-test periods are detailed in Appendix A.1.
Implementation.Input features are constructed from
minute-level multivariate data. Models map the feature se-
quence to realized returns and are optimized using AdamW.
During training, the supervision signal is dynamically de-
termined by our bi-level optimization framework, which
learns the optimal label horizon. Comprehensive details are
provided in Appendix A.5.
5.2. Baselines and Metrics
Baselines.To ensure a comprehensive and rigorous evalu-
ation, we benchmark our approach against a diverse set of
state-of-the-art models. Specifically, we select ten represen-
tative baselines spanning five distinct deep forecasting fami-
lies to cover a wide range of temporal modeling paradigms.
These includeLinear-based models(DLinear (Zeng et al.,
2023) and RLinear (Li et al., 2023)), which utilize sim-
ple yet effective linear mappings;RNN-based networks
(GRU (Dey & Salem, 2017) and LSTM (Hochreiter &
Schmidhuber, 1997)), representing classical sequential mod-
eling approaches;CNN-based architectures(TCN (Liu
et al., 2019) and ModernTCN (Luo & Wang, 2024)), which
capture local temporal dependencies through convolutions;
Transformer-based models(PatchTST (Nie et al., 2022)
and iTransformer (Liu et al., 2024b)), representing attention-
based forecasting paradigms; andSSM-based models
(Mamba (Gu & Dao, 2024) and Bi-Mamba+ (Liang et al.,
2024)), representing the latest advancements in structured
state space models.
Metrics.Performance is assessed across two dimensions:
Predictive Signal Quality, measured by the Pearson corre-
lation (IC) and Spearman rank correlation (RankIC), along
with their stability ratios (ICIR, RankICIR); and Investment
Potential, evaluated by the average daily return of the top
10% stocks, reporting the Daily Return and Sharpe Ratio.
7

## PDF page 8

The Label Horizon Paradox: Rethinking Supervision Targets in Financial Forecasting
Detailed descriptions of these baselines and metric calcula-
tions are provided in Appendix B.
5.3. Main Results
To align with standard benchmarks in the literature, we focus
our primary evaluation in the main text on the Daily Close-
to-Close setting (Scenario 1), comparing our framework
against the conventional baseline trained strictly on the final
target horizon r∆
t . As shown in Table 1, our bi-level method
consistently outperforms the standard paradigm across all
ten diverse architectures—ranging from classical RNNs and
linear models to state-of-the-art Transformers and SSMs—
and across all three market capitalization indices (CSI 300,
500, and 1000). Notably, our method not only enhances raw
predictive accuracy (IC and RankIC) but also yields substan-
tial improvements in signal stability (ICIR and RankICIR)
and portfolio simulation metrics (Top Return and Sharpe
Ratio). This universal improvement validates that relaxing
the strict label-target alignment can fundamentally enhance
representation learning in noisy financial environments.
Beyond standard interday predictions, we extend our eval-
uation to different temporal granularities. As detailed in
Appendix E.1, the results under intraday scenarios per-
fectly align with our theoretical expectations. In the highly
momentum-driven 30-minute window (Scenario 2), our
method automatically recovers the canonical target, per-
forming on par with the baseline. In the longer 90-minute
window (Scenario 3), our adaptive horizon selection success-
fully captures the intermediate optimal signal, delivering
notable gains in signal stability.
To ensure our findings are not artifacts of a specific market
or historical period, we conduct extensive cross-market and
out-of-distribution validations. Specifically, our framework
maintains consistent performance improvements on the US
S&P 500 index (Appendix E.3), confirming that the Label
Horizon Paradox holds even in highly efficient markets.
Furthermore, stress tests conducted during the severe market
crash and continuous downtrend of 2024 (Appendix E.4)
demonstrate that dynamic label selection provides crucial
risk resilience under extreme macroeconomic shocks.
Finally, while statistical metrics are informative, real-world
quantitative trading is constrained by market frictions. In
Appendix E.5, we present a simple downstream portfo-
lio backtest incorporating transaction costs, slippage, and
TW AP execution. Our method consistently generates higher
annualized returns while effectively reducing maximum
drawdowns (MDD) across backbones. Crucially, as ana-
lyzed in Appendix F, these comprehensive performance and
economic gains are achieved with only marginal computa-
tional overhead, thanks to the efficiency of our single-step
inner-loop design.
Table 2.Performance Comparison.Experiments are conducted
using an LSTM backbone across Scenarios 1, 2, and 3 on CSI 500.
We compare our proposed method (*) against two baselines: Naive
Averaging (†) and Equal-Weight Multi-Task Learning (‡).
CONFIGURATIONIC(×10) ICIR RANKIC(×10) RANKICIR
SCENARIO1∗ 1.029 0.861 0.859 0.895
SCENARIO1† 0.969 0.778 0.821 0.817
SCENARIO1‡ 0.932 0.803 0.814 0.837
SCENARIO2∗ 1.4911.3961.943 2.062
SCENARIO2† 1.4531.4711.857 2.021
SCENARIO2‡ 1.435 1.456 1.849 1.998
SCENARIO3∗ 1.0821.0951.399 1.609
SCENARIO3† 1.0501.1251.359 1.538
SCENARIO3‡ 1.071 1.118 1.367 1.596
6. Further Analysis
In this section, we conduct a series of in-depth analyses to
dissect the internal mechanisms of our framework.
6.1. Necessity of Bi-level Optimization
A natural question arises:can we achieve similar benefits
by simply averaging potential labels or treating them as
equal multi-task targets?To investigate this, we compare
our method against two baselines:
1. Naive Averaging:The model is trained on a single fixed
label ¯yt, constructed as the arithmetic mean of all candidate
proxy horizons (¯yt = 1
∆
P
δ zδ
t ).
2. Equal-Weight MTL:The model predicts all candidate
horizons simultaneously using a multi-task learning objec-
tive with fixed, equal weights (L= 1
∆
P
δ ℓ(ˆyt,r δ
t)).
As shown in Table 2, our Bi-level approach still outperforms
both methods. Naive Averaging tends to dilute the predictive
signal, as it indiscriminately mixes high-quality intermedi-
ate horizons with noisy ones. Similarly, Equal-Weight MTL
fails to prioritize, forcing the model to allocate capacity to
horizons that may contain little learnable information. In
contrast, our BLO framework dynamically up-weights the
most effective horizons based on validation feedback, prov-
ing that adaptive selection is superior to blind aggregation.
More detailed experiments and discussions are provided in
the Appendix E.2.
6.2. Alignment of Learned Weights with the Optima
A central claim of our work is that the proposed method acts
as an automatic signal-to-noise ratio detector. To verify this,
we visualize the final distribution of the learned horizon
weights λ and compare them against the empirical paradox
curve (the actual test IC of models trained on fixed horizons,
as observed in Section 3).
Figure 4 reveals a striking alignment. The peak of the
8

## PDF page 9

The Label Horizon Paradox: Rethinking Supervision Targets in Financial Forecasting
0 24 48 72 96 120 144 168 192 216
0 3 6 9 12 15 18 21 24 27
0 9 18 27 36 45 54 63 72 81
0 9 18 27 36 45 54 63 72 81
0.004
0.005
0.030
0.035
0.010
0.013
0.010
0.020
Figure 4.Visualization of Learned Horizon Weights ( λ).We
illustrate the final distribution of λ learned by an LSTM model
on the CSI500 dataset. The panels correspond to Scenario 1 (top),
Scenario 2 (second), Scenario 3 (third), and Scenario 3 without
warm-up (bottom).
learned weight distribution λ coincides closely with the
horizon that achieved the highest test IC in our brute-force
grid search. This indicates that the outer-loop gradient suc-
cessfully senses the signal-noise trade-off, navigating the
optimization focus toward the sweet spot of supervision.
6.3. Impact of Warm-up Phase
As visualized in the bottom row of Figure 4, omitting the
warm-up phase leads to a degenerate behavior in the label
distribution: the learned weights λ skew disproportionately
toward the earliest horizons, effectively discarding the infor-
mation embedded in longer timeframes.
From an optimization perspective, this phenomenon closely
mirrors the concept of shortcut learning (Geirhos et al.,
2020). Because short-horizon labels are temporally closer
to the input features, they naturally exhibit stronger correla-
tions. Consequently, they offer an “easy” path for rapid loss
reduction. When the bi-level optimization begins from a
completely untrained state, the single-step inner loop greed-
ily exploits these highly correlated but ultimately myopic
targets to minimize the immediate training objective.
However, while this greedy exploitation enables very fast
initial convergence, it fundamentally limits the model’s
predictive capacity. By fixating solely on the easiest-to-
predict short-term dynamics, the network fails to capture
the broader, more robust market trends, thereby imposing a
strictly low performance ceiling.
Therefore, the warm-up phase serves as a necessary struc-
tural prior. This ensures that when the dynamic weight
optimization is finally engaged, the model evaluates the
utility of different horizons based on meaningful feature rep-
resentations, effectively preventing the bi-level optimization
from getting trapped in trivial local minima.
7. Related Works
Our work addresses the inherent challenges of financial
forecasting by rethinking the definition and optimization of
supervision signals. Prior research primarily mitigates noise
through robust feature extraction (Feng et al., 2019) or by
applying noisy-label learning techniques (Zhang & Sabuncu,
2018; Reed et al., 2014) to construct cleaner training data
(Zeng et al., 2024), yet these methods typically operate
under a fixed prediction horizon. Consequently, they neglect
the dynamic trade-off between signal realization and noise
accumulation inherent in the label’s temporal evolution.
It is also important to distinguish our approach from stan-
dard label smoothing techniques (M¨uller et al., 2019). While
traditional label smoothing acts as a regularizer by softening
the numerical distribution of a fixed target (e.g., convert-
ing hard one-hot labels to soft probabilities), our method
operates orthogonally along the time axis. We do not al-
ter the inherent cross-sectional distribution of the return
labels; rather, we dynamically search for the optimal tempo-
ral horizon to serve as the supervision signal. Furthermore,
while one might intuitively attempt to “smooth” labels by
averaging targets across multiple horizons, our analysis in
Section 6.1 demonstrates that our adaptive horizon selection
is fundamentally distinct from, and strictly superior to, such
naive temporal mixing.
To exploit this unexamined temporal dimension, we adopt a
bi-level optimization framework. While such frameworks
have been widely employed for sample re-weighting (Ren
et al., 2018; Shu et al., 2019; Jiang et al., 2018) to filter noisy
training data, we diverge by extending this paradigm from
sample selection to label selection. Instead of cleaning input
samples, our approach utilizes it to dynamically search for
the optimal supervision horizon, effectively navigating the
evolving signal-noise trade-off.
8. Conclusion
This study identifies the Label Horizon Paradox, challenging
the conventional wisdom that training labels must strictly
align with inference targets. We reveal that optimal gen-
eralization requires decoupling the two to balance signal
emergence against market noise. By employing a bi-level
framework to autonomously learn the optimal supervision
horizon, our approach consistently enhances the perfor-
mance of diverse existing architectures. Ultimately, this
work establishes a new paradigm for dynamic, label-centric
optimization in highly stochastic forecasting environments.
9

## PDF page 10

The Label Horizon Paradox: Rethinking Supervision Targets in Financial Forecasting
Impact Statement
This research is intended solely for academic purposes. The
methodologies, models, and empirical results presented
herein do not constitute financial, legal, or investment ad-
vice, and the authors assume no responsibility for any fi-
nancial losses or adverse consequences arising from their
application in real-world trading environments. Further-
more, from an ethical data perspective, all experiments were
conducted using strictly publicly available market data (e.g.,
CSI 300, 500, 1000, and the US S&P 500). No private,
sensitive, or personally identifiable information (PII) of indi-
vidual investors was utilized, ensuring full compliance with
data privacy standards.
References
Al-Khasawneh, M. A., Raza, A., Khan, S. U. R., and Khan,
Z. Stock market trend prediction using deep learning
approach.Computational Economics, 66(1):453–484,
2025.
Alain, G. and Bengio, Y . Understanding intermediate
layers using linear classifier probes.arXiv preprint
arXiv:1610.01644, 2016.
Ang, A., Hodrick, R. J., Xing, Y ., and Zhang, X. The cross-
section of volatility and expected returns.The Journal of
Finance, 61(1):259–299, 2006.
Belkin, M., Hsu, D., Ma, S., and Mandal, S. Reconciling
modern machine-learning practice and the classical bias–
variance trade-off.Proceedings of the National Academy
of Sciences, 116(32):15849–15854, 2019.
Bengio, Y ., Courville, A., and Vincent, P. Representation
learning: A review and new perspectives.IEEE Transac-
tions on Pattern Analysis and Machine Intelligence, 35
(8):1798–1828, 2013.
Chen, C., Chen, X., Ma, C., Liu, Z., and Liu, X. Gradient-
based bi-level optimization for deep learning: A survey.
arXiv preprint arXiv:2207.11719, 2022.
Chen, L., Liu, S., Yan, J., Wang, X., Liu, H., Li, C., Jiao,
K., Ying, J., Liu, Y . V ., Yang, Q., et al. Advancing
financial engineering with foundation models: progress,
applications, and challenges.Engineering, 2025.
Chen, W. and Wang, Y . DHMoE: Diffusion generated hier-
archical multi-granular expertise for stock prediction. In
Proceedings of the AAAI Conference on Artificial Intelli-
gence, volume 39, pp. 11490–11499, 2025.
Dey, R. and Salem, F. M. Gate-variants of gated recurrent
unit (GRU) neural networks. In2017 IEEE 60th Inter-
national Midwest Symposium on Circuits and Systems
(MWSCAS), pp. 1597–1600. IEEE, 2017.
Feng, F., Chen, H., He, X., Ding, J., Sun, M., and Chua,
T.-S. Enhancing stock movement prediction with ad-
versarial training. InProceedings of the Twenty-Eighth
International Joint Conference on Artificial Intelligence,
pp. 5843–5849, 2019.
Franceschi, L., Frasconi, P., Salzo, S., Grazzi, R., and Pontil,
M. Bilevel programming for hyperparameter optimiza-
tion and meta-learning. InInternational Conference on
Machine Learning, pp. 1568–1577. PMLR, 2018.
Geirhos, R., Jacobsen, J.-H., Michaelis, C., Zemel, R., Bren-
del, W., Bethge, M., and Wichmann, F. A. Shortcut learn-
ing in deep neural networks.Nature Machine Intelligence,
2(11):665–673, 2020.
Grinold, R. C. and Kahn, R. N.Active portfolio management.
McGraw-Hill, 2000.
Gu, A. and Dao, T. Mamba: Linear-time sequence model-
ing with selective state spaces. InFirst Conference on
Language Modeling, 2024.
Hochreiter, S. and Schmidhuber, J. Long short-term memory.
Neural Computation, 9(8):1735–1780, 1997.
Hong, H. and Stein, J. C. A unified theory of underreaction,
momentum trading, and overreaction in asset markets.
The Journal of Finance, 54(6):2143–2184, 1999.
Jacot, A., Gabriel, F., and Hongler, C. Neural tangent ker-
nel: Convergence and generalization in neural networks.
InAdvances in Neural Information Processing Systems,
volume 31, 2018.
Jiang, G. J., Xu, D., and Yao, T. The information con-
tent of idiosyncratic volatility.Journal of Financial and
Quantitative Analysis, 44(1):1–28, 2009.
Jiang, L., Zhou, Z., Leung, T., Li, L.-J., and Fei-Fei, L.
MentorNet: Learning data-driven curriculum for very
deep neural networks on corrupted labels. InInterna-
tional Conference on Machine Learning, pp. 2304–2313.
PMLR, 2018.
Kenett, D. Y ., Huang, X., V odenska, I., Havlin, S., and
Stanley, H. E. Partial correlation analysis: Applications
for financial markets.Quantitative Finance, 15(4):569–
578, 2015.
Li, Z., Qi, S., Li, Y ., and Xu, Z. Revisiting long-term time
series forecasting: An investigation on linear mapping.
arXiv preprint arXiv:2305.10721, 2023.
Liang, A., Jiang, X., Sun, Y ., Shi, X., and Li, K. Bi-Mamba+:
Bidirectional mamba for time series forecasting.arXiv
preprint arXiv:2404.15772, 2024.
10

## PDF page 11

The Label Horizon Paradox: Rethinking Supervision Targets in Financial Forecasting
Linnainmaa, J. T. and Roberts, M. R. The history of the
cross-section of stock returns.The Review of Financial
Studies, 31(7):2606–2649, 2018.
Liu, M., Zhu, M., Wang, X., Ma, G., Yin, J., and Zheng,
X. Echo-gl: Earnings calls-driven heterogeneous graph
learning for stock movement prediction. InProceedings
of the AAAI Conference on Artificial Intelligence, vol-
ume 38, pp. 13972–13980, 2024a.
Liu, S., Yan, J., Wang, X., Jiang, Y ., Chen, L., Fan, T.,
Chen, K., and Yang, Q. Federated financial reasoning
distillation: Training a small financial expert by learning
from multiple teachers. InProceedings of the 6th ACM
International Conference on AI in Finance, pp. 623–631,
2025.
Liu, Y ., Dong, H., Wang, X., and Han, S. Time series
prediction based on temporal convolutional network. In
2019 IEEE/ACIS 18th International Conference on Com-
puter and Information Science (ICIS), pp. 300–305. IEEE,
2019.
Liu, Y ., Hu, T., Zhang, H., Wu, H., Wang, S., Ma, L., and
Long, M. iTransformer: Inverted transformers are effec-
tive for time series forecasting. InThe Twelfth Interna-
tional Conference on Learning Representations, 2024b.
Luo, D. and Wang, X. ModernTCN: A modern pure convo-
lution structure for general time series analysis. InThe
Twelfth International Conference on Learning Represen-
tations, 2024.
M¨uller, R., Kornblith, S., and Hinton, G. E. When does
label smoothing help?Advances in Neural Information
Processing Systems, 32, 2019.
Nie, Y ., Nguyen, N. H., Sinthong, P., and Kalagnanam, J. A
time series is worth 64 words: Long-term forecasting with
transformers.arXiv preprint arXiv:2211.14730, 2022.
Reed, S., Lee, H., Anguelov, D., Szegedy, C., Erhan, D., and
Rabinovich, A. Training deep neural networks on noisy la-
bels with bootstrapping.arXiv preprint arXiv:1412.6596,
2014.
Reinganum, M. R. The arbitrage pricing theory: Some
empirical results.The Journal of Finance, 36(2):313–
321, 1981.
Ren, M., Zeng, W., Yang, B., and Urtasun, R. Learning to
reweight examples for robust deep learning. InInterna-
tional Conference on Machine Learning, pp. 4334–4343.
PMLR, 2018.
Sawhney, R., Agarwal, S., Wadhwa, A., and Shah, R. Deep
attentive learning for stock movement prediction from so-
cial media text and company correlations. InProceedings
of the 2020 Conference on Empirical Methods in Natural
Language Processing (EMNLP), pp. 8415–8426, 2020.
Shah, J., Vaidya, D., and Shah, M. A comprehensive review
on multiple hybrid deep learning approaches for stock
prediction.Intelligent Systems with Applications, 16:
200111, 2022.
Shi, H., Song, W., Zhang, X., Shi, J., Luo, C., Ao, X.,
Arian, H., and Seco, L. A. Alphaforge: A framework
to mine and dynamically combine formulaic alpha fac-
tors. InProceedings of the AAAI Conference on Artificial
Intelligence, volume 39, pp. 12524–12532, 2025.
Shleifer, A.Inefficient markets: An introduction to be-
havioural finance. OUP Oxford, 2000.
Shu, J., Xie, Q., Yi, L., Zhao, Q., Zhou, S., Xu, Z., and
Meng, D. Meta-Weight-Net: Learning an explicit map-
ping for sample weighting. InAdvances in Neural Infor-
mation Processing Systems, volume 32, 2019.
Sonkavde, G., Dharrao, D. S., Bongale, A. M., Deokate,
S. T., Doreswamy, D., and Bhat, S. K. Forecasting stock
market prices using machine learning and deep learn-
ing models: A systematic review, performance analysis
and discussion of implications.International Journal of
Financial Studies, 11(3):94, 2023.
Wang, M., Ma, T., and Cohen, S. B. Pre-training time series
models with stock data customization. InProceedings
of the 31st ACM SIGKDD Conference on Knowledge
Discovery and Data Mining, pp. 3019–3030, 2025.
Yu, S., Xue, H., Ao, X., Pan, F., He, J., Tu, D., and He,
Q. Generating synergistic formulaic alpha collections via
reinforcement learning. InProceedings of the 29th ACM
SIGKDD Conference on Knowledge Discovery and Data
Mining, pp. 5476–5486, 2023.
Zeng, A., Chen, M., Zhang, L., and Xu, Q. Are transform-
ers effective for time series forecasting? InProceedings
of the AAAI Conference on Artificial Intelligence, vol-
ume 37, pp. 11121–11128, 2023.
Zeng, L., Wang, L., Niu, H., Zhang, R., Wang, L., and
Li, J. Trade when opportunity comes: price movement
forecasting via locality-aware attention and iterative re-
finement labeling. InProceedings of the Thirty-Third
International Joint Conference on Artificial Intelligence,
pp. 6134–6142, 2024.
Zhang, Z. and Sabuncu, M. R. Generalized cross entropy
loss for training deep neural networks with noisy labels.
InAdvances in Neural Information Processing Systems,
volume 31, 2018.
11

## PDF page 12

The Label Horizon Paradox: Rethinking Supervision Targets in Financial Forecasting
A. Experimental Setup
A.1. Data and Universe
Our empirical study is comprehensively evaluated across diverse market environments, including the Chinese A-share
market and the US equity market. For our primary evaluation, we focus on three widely recognized A-share indices: CSI
300, CSI 500, and CSI 1000, which correspond to large-, medium-, and small-cap stocks, respectively, thereby ensuring that
our dataset is highly representative of the broader market.
To ensure a robust evaluation and prevent look-ahead bias, we employ strict chronological splits. The data spans from
January 2018 to July 2025, partitioned into three distinct settings based on the experimental scenarios:
• Standard Setting (CSI 300/500/1000 & S&P 500):Used for the main results and the US market generalization
experiment.
– Training Set:January 2019 – July 2023.
– Validation Set:July 2023 – July 2024.
– Test Set:July 2024 – July 2025.
• Stress Test Setting (CSI 500):Shifted to cover a severe and continuous macroeconomic downtrend, culminating in
the February 2024 market crash.
– Training Set:January 2018 – July 2022.
– Validation Set:July 2022 – July 2023.
– Test Set:July 2023 – July 2024.
A.2. Raw Data
For each stock i on day t, the raw data is an intraday multivariate time series consisting of 7 variables: Open Price, High
Price, Low Price, Close Price, Amount, V olume, and Transaction Count. These variables are sampled at 1-minute intervals.
Depending on the market, the length of the daily sequence varies to match the respective trading hours:
• A-share Market:The sequence covers the 240 minutes of a standard trading day (9:30 AM to 11:30 AM and 1:00 PM
to 3:00 PM, totaling 4 hours), denoted asV i,t ∈R 240×7.
• US Market:The sequence is extended to cover the longer daily trading session (9:30 AM to 4:00 PM, totaling 6.5
hours), denoted asV i,t ∈R 390×7.
A.3. Feature Engineering
To maintain computational tractability while preserving microstructure information, we divide the raw sequence into
non-overlapping patches. Each patch contains 15 minutes of trading data, from which we extract statistical descriptors to
form the model input. Within each patch, we extract a diverse set of statistical descriptors to characterize the local market
state from multiple dimensions. Specifically, for each of the raw variables, we compute a broad spectrum of univariate
descriptors, including momentum and scale measures such as the arithmetic mean, the change rate, and the normalized range.
To capture the distribution shape and potential fat-tail characteristics within the window, we further incorporate higher-order
moments, exemplified by the standard deviation, skewness, and kurtosis. Beyond univariate analysis, we employ a wide
variety of bivariate interaction descriptors to model the dynamic coupling between different market facets. These descriptors
encompass linear coupling measures—for instance, the Pearson correlation coefficient for key pairs like price-volume—as
well as relative intensity ratios, such as volume per transaction and other scale-invariant metrics. Due to the extensive nature
of the feature set, we refrain from enumerating every specific indicator and focus here on these representative categories. All
extracted features are concatenated into a consolidated tensor with D dimensions, providing a high-fidelity representation of
the microstructure for subsequent model input.
12

## PDF page 13

The Label Horizon Paradox: Rethinking Supervision Targets in Financial Forecasting
A.4. Scenario-Specific Configuration
To strictly align with the three market scenarios defined in the main text, we construct specific input tensors based on the
decision time t. Let D denote the feature dimension per patch. The input configurations are defined as follows (Scenario
1 is evaluated on both the A-share and the US S&P 500 markets, whereas Scenarios 2 and 3 are considered only for the
A-share market):
Scenario 1: Interday (Standard) Prediction.The decision time t corresponds to the market close. The input xi,t
aggregates the entire trading day’s microstructure information. For the A-share market, this consists of 16 patches (covering
the full 240-minute trading session), resulting in an input tensor shape of xi,t ∈R 16×D. For the US S&P 500 market,
this consists of 26 patches (covering the 390-minute session), resulting in xi,t ∈R 26×D. The objective is to predict the
return of the next trading day (∆ = 1day ), calculated based on the last price of the continuous session to preserve temporal
continuity.
Scenario 2: Intraday (30-minute) Prediction.The decision time t is set at the midpoint of the trading session (11:30,
Morning Close), leveraging the market’s distinct morning/afternoon session structure. To prevent look-ahead bias, the
input utilizes only the morning session data (09:30–11:30), resulting in a sequence of 8 patches. The input tensor shape is
xi,t ∈R 8×D. The objective is to predict the return over the subsequent 30-minute interval (∆ = 30min).
Scenario 3: Intraday (90-minute) Prediction.The decision time t is also set at the midpoint of the trading session (11:30).
Similar to Scenario 2, the input is derived exclusively from the morning session, maintaining an identical input tensor shape
of xi,t ∈R 8×D. However, the forecasting objective here is to predict the return over the subsequent 90-minute interval
(∆ = 90min), capturing a longer intraday trend than Scenario 2.
A.5. Implementation Details
A.5.1. PREDICTIVEMODELTRAINING
Input features are constructed from minute-level multivariate market data. The predictive model maps this feature sequence
to the designated label (i.e., the return at the specific horizon determined by the experimental setting).
Training Configuration.We set the batch to cover 20 trading days, i.e., one batch contains data from a 20-day window. All
models are optimized using the AdamW optimizer with MSE loss. Importantly, we standardize both the model outputs and
the labels cross-sectionally (zero mean and unit variance). Under this normalization, minimizing the MSE is equivalent to
maximizing the Pearson correlation (IC) between predictions and labels, since for standardized variables
MSE(ˆy, y) =E[(ˆy−y)2] = 2−2Corr(ˆy, y),(15)
so both objectives are aligned up to an affine transformation.
Early Stopping Strategy.We employ an early stopping mechanism to prevent overfitting. During training, the loss on
the validation set is monitored at the end of every epoch. The training process is terminated if the validation loss does not
improve for 5 consecutive epochs (patience = 5). Upon termination, the model parameters corresponding to the lowest
validation loss are restored as the final model.
A.5.2. BI-LEVELOPTIMIZATIONTRAINING.
The training of our Label-Horizon-based bi-level framework proceeds in two stages: a warm-up stage and a bi-level iteration
stage.
Warm-up Stage.Before initiating the alternating optimization of the model parameters and the horizon parameter, we
perform a warm-up phase to stabilize the model weights. The warm-up lasts for Nwarm = 3 epochs. During this phase, the
training configuration (learning rate, batch construction) is identical to the standard predictive model training described
above.
Bi-level Iteration Stage.Following the warm-up, we proceed with the bi-level updates. To strictly separate the data used
for the inner loop (model update) and the outer loop (horizon update), we employ a date-based random splitting strategy:
• Data Splitting:For each batch containing 20 trading days, the days are randomly divided into two equal subsets (10
days each). The first subset serves as the support set (for the inner loop), and the second subset serves as the query set
13

## PDF page 14

The Label Horizon Paradox: Rethinking Supervision Targets in Financial Forecasting
for the outer loop.
• Inner Loop (Model Update):The model parameters are updated using the support set. The weights λ are obtained by
normalizing a set of learnable parameters via a softmax transformation. Since the model has been pre-trained during
the warmup phase, we use a reduced learning rate1×10 −6 for fine-tuning.
• Outer Loop (Horizon Update):The horizon parameter is updated using the query set. The learning rate for the outer
loop is set to1×10 −3 and the weight of the entropy term is set to1×10 −3.
14

## PDF page 15

The Label Horizon Paradox: Rethinking Supervision Targets in Financial Forecasting
B. Baselines and Metrics
B.1. Baseline Models
To ensure the robustness of our findings and position our method within the broader landscape of deep time-series forecasting,
we benchmark across five distinct architectural families. These baselines range from classical sequence models to the latest
state-of-the-art foundation models:
• RNN-based Methods:We include GRU and LSTM. These recurrent architectures serve as the traditional workhorses
for financial sequence modeling, processing data sequentially to capture temporal dependencies, though often struggling
with long-term memory retention.
• Linear/MLP-based Methods:Despite the rise of complex architectures, simple linear models have shown surprising
effectiveness in noisy time-series tasks. We compare against DLinear, which employs a trend-seasonal decomposition
combined with linear layers, and RLinear, which focuses on reversible normalization to handle distribution shifts.
• CNN-based Methods:To evaluate convolutional approaches, we select TCN, which utilizes dilated causal convolutions
to model long-range history with a receptive field that grows exponentially. We also include ModernTCN, a recent
adaptation that incorporates large-kernel convolutions and parameter-efficient designs.
• Transformer-based Methods:we employ PatchTST and iTransformer. PatchTST segments time series into patches
and applies channel-independent attention to capture local semantic patterns, while iTransformer inverts the attention
mechanism to model the correlation between multivariate variates directly, making it particularly relevant for capturing
cross-stock interactions.
• SSM-based Methods:We assess the emerging class of Selective State Space Models (SSMs) via Mamba and Bi-
Mamba+. These models utilize a hardware-efficient selection mechanism to achieve linear computational complexity
relative to sequence length, theoretically allowing for superior modeling of long contexts without the quadratic cost of
Transformers.
B.2. Evaluation Metrics
We evaluate model performance using a comprehensive set of metrics that assess both the statistical predictive power and
the practical economic value of the generated signals.
Predictive Accuracy Metrics.These metrics measure the correlation between the model’s output signal and the ground-
truth future returns, focusing on the signal’s information content.
• IC (Information Coefficient):Defined as the Pearson correlation coefficient between the predicted scores and the
realized returns across the cross-section of stocks at each time step. We report the time-series mean of the daily IC.
• ICIR (Information Ratio):A measure of prediction stability, calculated as the ratio of the mean IC to the standard
deviation of the IC (Mean(IC)/Std(IC)). A higher ICIR indicates a more consistent signal performance.
• RankIC & RankICIR:Given that financial returns often contain outliers, we also report the Spearman rank correlation
(RankIC) and its corresponding stability ratio (RankICIR). Rank-based metrics are robust to extreme values and more
accurately reflect the sorting capability required for portfolio construction.
Portfolio Simulation Metrics.To gauge the model’s predictive power, we focus on the performance of the top-ranked
stocks. Specifically, at each decision time, we calculate the equal-weighted average daily return of the top 10% of stocks
with the highest predicted scores.
• Top Returns:The average daily return of the top 10% of stocks ranked by predicted values, where, for all three
forecasting scenarios, we generate predictions once per day and compute this metric using the corresponding horizon-
specific realized returns.
15

## PDF page 16

The Label Horizon Paradox: Rethinking Supervision Targets in Financial Forecasting
•Sharpe Ratio:The risk-adjusted return, calculated as the mean of the daily returns divided by the standard deviation
of these daily returns. This metric indicates the daily return generated per unit of risk. In our experiments, we report
the annualized Sharpe Ratio by multiplying the daily Sharpe by
√
252.
While our primary evaluation focuses on the predictive quality and stability of the learned signals to cleanly elucidate the
Label Horizon Paradox, we also recognize the importance of practical economic value. Therefore, in addition to the Top
Returns and Sharpe Ratio metrics evaluated directly on the signals, we conduct a simple downstream portfolio backtesting
simulation—incorporating transaction costs, slippage, and TW AP execution—detailed in Appendix E.5.
16

## PDF page 17

The Label Horizon Paradox: Rethinking Supervision Targets in Financial Forecasting
C. Theoretical Analysis with a Linear Factor Model
In this section, we provide a rigorous theoretical justification for the Label Horizon Paradox. We construct a theoretical
framework grounded in the Arbitrage Pricing Theory (APT). We begin with the standard static APT model and extend it
into a continuous-time setting to explicitly capture the dynamics of signal realization and noise accumulation.
Our goal is to derive the generalization performance (Information Coefficient) of a linear estimator trained on a proxy
horizon return rδ and evaluated on the final target horizon return r∆. For notational brevity, we omit the decision time
subscripttand the stock indexiin the subsequent analysis.
C.1. Data Generating Process: A Time-Varying APT Extension
We consider a universe of stocks where returns are driven by observable factors.
C.1.1. THESTANDARDSTATICAPT
In the classical APT framework, the return of a stock over a fixed period is decomposed into a systematic component driven
by common factorssand an idiosyncratic component. Using our notation:
r∆ =w ∗⊤s+ϵ ∆,(16)
where s represents factor exposures, w∗ represents factor risk premia, and ϵ∆ is the idiosyncratic noise. This model is
typically static—it describes the return over a single, undefined period where information is assumed to be fully reflected.
C.1.2. TEMPORALEXTENSION
We extend the standard APT by introducing a continuous time parameterδ∈(0,∆]to model the trajectory of returns.
First, we formally define the signal and weight components with the following assumptions:
• Factor Exposure s:Let s∈R d be the vector of factor exposures (predictive signals) for a stock at the decision time t.
We assume factors are whitened such thatE[ss ⊤] =I d.
• True Factor Loadings w∗:Let w∗ ∈R d represent the latent, ground-truth linear relationship between factors and
returns. We assume ∥w∗∥2 = 1 for identifiability (a normalization that fixes the scale between α(δ) and w∗ and
simplifies the derivations).
For any cumulative returnr δ from the decision timettot+δ, we propose the following time-varying specification:
rδ =α(δ)|{z}
Signal Realization
w∗⊤s+ϵ δ
|{z}
Accumulated Noise
.(17)
This formulation can be interpreted as a snapshot of the APT model at a specific horizon δ. Compared to the standard
baseline, we introduce two critical time-dependent modifications:
1. Signal Realization Process (α(δ)):Unlike the standard APT, which assumes equilibrium (i.e., information is fully
priced), we acknowledge that information incorporation takes time. Let α: (0,∆]→(0, A] be a monotonically
increasing function representing the degree of price discovery, where A >0 is a finite upper bound determined by the
overall scale of the latent signal.
•α(δ)< Aimplies partial underreaction or gradual diffusion of information.
•α(δ)≈Aimplies the signal is (effectively) fully realized at that horizon.
2. Noise Accumulation Process (ϵδ):We explicitly model the idiosyncratic term ϵδ as a dynamic process rather than a
static error. Consistent with the Random Walk Hypothesis (Brownian motion) for efficient markets, we assume the
noise is jointly defined across horizons as a microstructure-shifted Brownian motion:
ϵδ =η 0 +σW δ, η 0 ∼ N(0, σ 2δ0), W δ is a standard Brownian motion,(18)
17

## PDF page 18

The Label Horizon Paradox: Rethinking Supervision Targets in Financial Forecasting
where σ2 is the accumulation rate of idiosyncratic volatility, and δ0 >0 represents intrinsic microstructure noise that
exists even asδ→0. This implies the marginal distribution
ϵδ ∼ N

0, σ2(δ+δ 0)

,(19)
and for any0< δ≤∆, the nested random-walk property
Cov(ϵδ, ϵ∆) = Var(ϵδ) =σ 2(δ+δ 0).(20)
While this assumption is generally reasonable at short horizons such as intraday (minute-level) and daily intervals,
it may become less accurate over much longer horizons where structural breaks and slow-moving factors dominate.
Since our study focuses on short-term stock forecasting at minute and daily frequencies, the random-walk-based noise
model is well aligned with the forecasting regimes of interest.
Relationship to Standard APT:For any fixed horizon δ, our model collapses to a standard linear factor model with effective
signal strength α(δ)w∗ and noise variance σ2(δ+δ 0). Structurally, this formulation assumes ahorizon-invariantsignal
direction: the latent predictive relationship w∗ remains constant, while the temporal dynamics are entirely captured by
the scalar realization function α(δ). While real-world factor exposures might exhibit rotations across different forecasting
horizons, this deliberate simplification serves a crucial theoretical purpose. By fixing the signal direction, we mathematically
isolate the fundamental temporal trade-off without the confounding effects of factor shifting. Consequently, the core of
the Label Horizon Paradox naturally emerges purely from the dynamic interplay between the derivative of α(δ) (signal
accumulation) and the derivative of the noise variance (noise accumulation). Extending this framework to accommodate
more complex dynamics, such as horizon-dependent factor rotations, remains a valuable direction for future research.
C.2. The Learning Setup: Finite-Sample OLS
Consider a training dataset D={(s j, rδ
j)}N
j=1 of size N, where the labels are realized returns at the proxy horizon δ. We
employ Ordinary Least Squares (OLS) to estimate the factor loadings.
The estimated weight vector ˆwδ is given by:
ˆwδ = (S⊤S)−1S⊤rδ =α(δ)w ∗ + (S⊤S)−1S⊤ϵδ.(21)
Assuming N is sufficiently large such that S⊤S≈NI d (due to the whitening assumption), the estimator decomposes into:
ˆwδ =α(δ)w ∗ +z δ,wherez δ ∼ N

0, σ2(δ+δ 0)
N Id

.(22)
The variance of the estimation error zδ grows linearly with δ, reflecting the difficulty of learning from long-horizon labels
dominated by accumulated random-walk noise.
C.3. Derivation of Generalization Performance (Final IC)
We define the Information Coefficient (IC) as the Pearson correlation between the model’s predictionˆy= ˆw⊤
δ s and the final
target returnr ∆, evaluated on an independent test set.
First, we derive the necessary variance and covariance terms:
•Covariance:Recall that
ˆyδ = ˆw⊤
δ s=

α(δ)w∗ +z δ
⊤
s=α(δ)w ∗⊤s+z ⊤
δ s,
and the target can be written as
r∆ =α(∆)w ∗⊤s+ϵ ∆.
By construction, the estimation noise zδ is independent of the test-time features s and the test noise ϵ∆, and has zero
mean. Using these facts and the whitening assumptionE[ss ⊤] =I d, together with∥w ∗∥2 = 1, we have
Cov(ˆyδ, r∆) =Cov

α(δ)w∗⊤s+z ⊤
δ s, α(∆)w ∗⊤s+ϵ ∆
(23)
=α(δ)α(∆)Var(w ∗⊤s) +Cov(z ⊤
δ s,w ∗⊤s)| {z }
=0
+Cov(α(δ)w ∗⊤s, ϵ∆)| {z }
=0
+Cov(z ⊤
δ s, ϵ∆)| {z }
=0
(24)
=α(δ)α(∆)·1 =α(δ)α(∆).(25)
18

## PDF page 19

The Label Horizon Paradox: Rethinking Supervision Targets in Financial Forecasting
Therefore, only the systematic signal component contributes to the covariance:
Cov(ˆyδ, r∆) =Cov(α(δ)w ∗⊤s, α(∆)w∗⊤s) =α(δ)α(∆).(26)
•Prediction Variance (V est):
Vest(δ) =Var( ˆw⊤
δ s) =α(δ) 2 + d
N σ2(δ+δ 0).(27)
•Target Variance (V target):
Vtarget =Var(r ∆) =α(∆) 2 +σ 2(∆ +δ 0).(28)
Combining these, the expected squared IC on the final target is:
J(δ)≜IC 2
final(δ) = Cov(ˆyδ, r∆)2
Vest(δ)Vtarget
= α(δ)2α(∆)2
[α(δ)2 +K(δ+δ 0)]·V target
,(29)
whereK= d
N σ2 is a constant.
C.4. Proof of the Paradox
To determine the optimal training horizon δ∗, we analyze the behavior of the expected squared IC, J(δ) . Since the target
variance Vtarget and α(∆) are constant scalars independent of the training horizon δ, maximizing J(δ) is equivalent to
maximizing the log-objective ofα(δ) 2/

α(δ)2 +K(δ+δ 0)

.
C.4.1. INTUITIVEPROOF: SIGNAL VS. NOISEACCUMULATION
We analyze the log-performance, which allows for an additive decomposition of the trade-off. Ignoring constant terms, the
objective function is:
lnJ(δ) = 2 lnα(δ)| {z }
Information Gain
−ln

α(δ)2 +K(δ+δ 0)

| {z }
Noise Penalty
+C.(30)
This decomposition reveals the structural mechanism behind the Label Horizon Paradox:
1. Information Gain:This term represents the logarithmic accumulation of the realized signal. It increases monotonically
asδgrows.
2. Noise Penalty:This term represents the penalty from the total prediction variance. Since the idiosyncratic noise
K(δ+δ 0)follows a random walk, this term grows strictly and indefinitely.
The Paradox Mechanism:At short horizons, the rapid realization of the signal dominates the noise, leading to performance
gains. However, as the horizon extends, signal growth naturally decelerates (diminishing returns), while noise accumulation
remains constant and linear. Therefore, a tipping point δ∗ is eventually reached where the steady accumulation of noise
overwhelms the benefit of the slowing signal, causing the final performance to decline.
C.4.2. MATHEMATICALDERIVATIVEANALYSIS
To determine the location of the optimal horizon δ∗, we examine the first derivative of the log-performance functionJ(δ) .
Differentiating Eq. (30) with respect toδyields the gradient:
d
dδ lnJ(δ) = 2α′(δ)
α(δ) − 2α(δ)α′(δ) +K
α(δ)2 +K(δ+δ 0) .(31)
To understand the sign of this derivative, we analyze the condition for performance improvement, i.e., d
dδ lnJ(δ)>0 .
Substituting Eq. (31) into this inequality gives:
19

## PDF page 20

The Label Horizon Paradox: Rethinking Supervision Targets in Financial Forecasting
2α′(δ)
α(δ) > 2α(δ)α′(δ) +K
α(δ)2 +K(δ+δ 0) .(32)
Assumingα(δ)>0andK >0, we can cross-multiply by the denominators without changing the inequality sign:
2α′(δ)

α(δ)2 +K(δ+δ 0)

> α(δ) [2α(δ)α′(δ) +K].(33)
Expanding both sides reveals a common term:
2α′(δ)α(δ)2 + 2α′(δ)K(δ+δ 0)>2α(δ) 2α′(δ) +α(δ)K.(34)
Subtracting the common term2α ′(δ)α(δ)2 from both sides, the inequality simplifies significantly:
2α′(δ)K(δ+δ 0)> α(δ)K.(35)
Finally, dividing by K and rearranging the terms to separate the signal dynamics from the time horizon, we obtain the
necessary and sufficient condition for the derivative to be positive:
α′(δ)
α(δ) > 1
2(δ+δ 0) .(36)
This inequality compares the relative growth rate of the signal ( α′
α ) with the hyperbolic decay rate of the noise horizon
( 1
2(δ+δ0)).
C.5. Detailed Mechanism Analysis of Different Horizon Scenarios
In this section, we apply the rigorous derivative analysis derived above to interpret the empirical results presented in Section
3.1. As established in Eq. (36), the shape of the performance curve J(δ) is determined entirely by the competition between
the relative signal growth rate and the inverse time horizon. The sign of the gradient depends on the condition:
α′(δ)
α(δ)|{z}
Signal Growth Rate
≷ 1
2(δ+δ 0)| {z }
Noise Threshold
.(37)
Scenario 1: Interday Prediction (Monotonic Decrease).In the standard daily prediction setting (predicting close-to-close
returns), empirical results consistently favor the shortest proxy (close-to-open). Theoretically, this implies that the relevant
information is priced in almost immediately at the market open.
•Mathematical Regime:Since the signal saturates early,α(δ)≈const andα ′(δ)≈0for almost allδ >0.
• Inequality Analysis:The Signal Growth Rate vanishes ( ≈0 ) while the Noise Threshold remains positive. Thus,
α′
α < 1
2(δ+δ0) holds for the entire duration.
•Conclusion:The derivative is strictly negative, rendering the shortest horizon optimal (δ ∗ →0).
Scenario 2: Intraday 30-minute Prediction (Monotonic Increase).For short-term 30-minute windows, the market
undergoes active price discovery driven by momentum that persists throughout the interval.
• Mathematical Regime:The signal α(δ) grows robustly across the short window, maintaining a high marginal gain
α′(δ).
• Inequality Analysis:The short duration keeps the Noise Threshold ( 1
2(δ+δ0)) comparable to the signal growth. Because
the interval is too short for the signal to saturate, the inequality α′
α > 1
2(δ+δ0) remains true up toδ= ∆.
20

## PDF page 21

The Label Horizon Paradox: Rethinking Supervision Targets in Financial Forecasting
•Conclusion:The derivative remains positive, suggesting that the model benefits from extending the proxy horizon to
the full target length (δ∗ = ∆).
Scenario 3: Intraday 90-minute Prediction (Hump-Shaped).When the target window extends to 90 minutes, we observe
the characteristic Label Horizon Paradox. This scenario represents the transition between active information diffusion and
signal saturation.
• Mathematical Regime:Initially, information flows rapidly ( α′ is large). However, as δ increases, the predictive
validity of the signal at timetnaturally decays or is fully incorporated into the price (α ′ →0).
•Inequality Analysis:
1. Early Phase: The rapid signal uptake ensures α′
α > 1
2(δ+δ0), driving performance up.
2. Late Phase: As signal growth slows, α′
α drops below the threshold 1
2(δ+δ0), meaning the marginal noise cost
exceeds the marginal information value.
• Conclusion:The gradient crosses from positive to negative at an intermediate point. The optimal horizon δ∗ is
precisely the instant where the relative signal growth equals the inverse time horizon.
C.6. Decomposition under Interday Prediction Scenario
We now apply the theoretical framework to Scenario 1 (Standard Daily Close-to-Close Prediction). In this setting, the input
features are historical data available at the close of day t. Given the overnight information processing period, the predictive
signal derived from these features is typically incorporated into prices immediately at the market open of dayt+ 1.
Mathematically, this corresponds to the regime of rapid price discovery. The signal realization function satisfiesα(δ)≈const
and α′(δ)≈0 for any horizon δ extending beyond the market open, and in particular α(δ)≈α(∆) across the relevant
horizons.
Under the general model rδ =α(δ)w ∗⊤s+ϵ δ and r∆ =α(∆)w ∗⊤s+ϵ ∆, and recalling that the idiosyncratic noise
follows a nested random-walk structure such that Cov(ϵδ, ϵ∆) =Var(ϵ δ), the covariance between the proxy label rδ and the
targetr ∆ is
Cov(rδ, r∆) =α(δ)α(∆)Var(w ∗⊤s) +Cov(ϵ δ, ϵ∆) =α(δ)α(∆) +σ 2(δ+δ 0).(38)
The proxy and target variances are given by
Vproxy(δ) =Var(r δ) =α(δ) 2 +σ 2(δ+δ 0),(39)
Vtarget =Var(r ∆) =α(∆) 2 +σ 2(∆ +δ 0).(40)
The corresponding correlations are
ρ(ˆyδ, rδ) = Cov(ˆyδ, rδ)√Vest
pVproxy
= α(δ)2
√Vest
pVproxy
,(41)
ρ(rδ, r∆) = Cov(rδ, r∆)pVproxy
pVtarget
= α(δ)α(∆) +σ 2(δ+δ 0)pVproxy
pVtarget
,(42)
and
ICfinal(δ) =ρ(ˆyδ, r∆) = Cov(ˆyδ, r∆)√Vest
pVtarget
= α(δ)α(∆)√Vest
pVtarget
.(43)
Combining these, the final Information Coefficient admits the following general multiplicative form:
ICfinal(δ) =ρ(ˆyδ, rδ)ρ(r δ, r∆) α(δ)α(∆)
α(δ)2 · Vproxy(δ)
α(δ)α(∆) +σ 2(δ+δ 0) .(44)
In the interday rapid price discovery regime, we have α(δ)≈α(∆) for all relevant proxy horizons. Substituting this into the
general expressions, the covariance between the proxy label and the target simplifies to
Cov(rδ, r∆) =α(δ)α(∆) +σ 2(δ+δ 0)≈α(δ) 2 +σ 2(δ+δ 0) =V proxy(δ).(45)
21

## PDF page 22

The Label Horizon Paradox: Rethinking Supervision Targets in Financial Forecasting
Under this approximation, the proxy effectively behaves as a noisy but nearly unbiased version of the target at the same
signal realization level, and the final IC is numerically close to the product of the model’s fit to the proxy and the proxy’s
correlation with the target:
ICfinal(δ)≈ρ(ˆy δ, rδ)×ρ(r δ, r∆).(46)
where:
•ρ(ˆyδ, rδ): Represents theProxy IC(how well the model learns the specific labelr δ).
•ρ(r δ, r∆): Represents theLabel Alignment(how well the proxyr δ correlates with the ultimate targetr ∆).
To rigorously validate this theoretical decomposition, we conducted an extensive empirical study. We trained independent
LSTM models across the full spectrum of intraday horizons at minute-level granularity. To ensure statistical robustness and
mitigate initialization noise, each horizon-specific model was trained using multiple random seeds. This evaluation was
performed across three major indices (CSI300, CSI500, and CSI1000).
For each model, we computed the actual test IC (ICfinal) and compared it against the product of the empirically measured
components ρ(ˆyδ, rδ) and ρ(rδ, r∆). As illustrated in Figure 3, the empirical results demonstrate a near-perfect alignment
between the theoretical decomposition and the actual performance. This validates that in the interday regime, the performance
dynamics are indeed governed by the fundamental trade-off between signal saturation and random walk noise accumulation,
as predicted by our modified APT framework.
22

## PDF page 23

The Label Horizon Paradox: Rethinking Supervision Targets in Financial Forecasting
D. Alternative Derivation via Partial Correlation Formula
In the main text, we derived the performance decomposition identity using a structural Linear Factor Model. In this appendix,
we provide an alternative derivation based purely on the statistical properties of correlation. Specifically, we show that the
decomposition can be rigorously understood as a special case of the Partial Correlation Formula where the residual term
vanishes due to the specific signal dynamics of the market. This shows that the multiplicative decomposition of the final IC
is not an artifact of the specific factor-model setup, but a direct consequence of the vanishing partial correlation between
the model prediction and the residual return beyond the proxy horizon. For notational brevity, we omit the decision time
subscripttand the stock indexiin the subsequent analysis.
D.1. The Decomposition and the Vanishing Residual
From a statistical perspective, the relationship between the model prediction ˆyδ, the proxy label rδ, and the final target r∆
can, under the standard linear/Gaussian framework, be expressed via the following correlation decomposition:
ρˆyδ,r∆ =ρ ˆyδ,rδ ·ρ rδ,r∆
| {z }
Mediated Path
+ρ ˆyδ,r∆·rδ
q
1−ρ 2
ˆyδ,rδ
q
1−ρ 2
rδ,r∆
| {z }
Residual Term
.(47)
Here, the notation is rigorously defined as follows:
•ρ A,B denotes the standard Pearson correlation coefficient between variables A and B, consistent with the definition of
IC used throughout the paper.
•ρ A,B·C denotes the partial correlation coefficient between A and B given a control variable C. As formally derived
in the subsequent section, this is defined as the Pearson correlation between the residuals of A and B after the linear
effect ofChas been regressed out (i.e.,ρ(e A|C, eB|C)).
The physical interpretation of this formula in our context provides deep insight into the Label Horizon Paradox:
• The Mediated Path represents the efficacy of the prediction insofar as it captures information already contained in the
proxy horizonδ.
• The Residual Term is controlled by the partial correlation ρˆyδ,r∆·rδ. This term measures the correlation between the
model’s prediction and the final target after the influence of the proxyrδ has been removed. Effectively, it asks:Can
the model predict the return evolution fromδto∆that is orthogonal to the return up toδ?
Application to Scenario 1 (Interday Prediction):In Scenario 1, the input features are derived from history prior to the
market open. Due to the high efficiency of the market, the predictive signal contained in these historical features is typically
priced in almost immediately upon the open.
Consequently, the subsequent price movement from the intermediate horizon δ to the final target ∆ is dominated by
new, idiosyncratic information and noise that was not available at the decision time. Since this future noise is strictly
unforecastable based on the input features, the model’s predictive power for this residual component is negligible.
Mathematically, this implies ρˆyδ,r∆·rδ ≈0 . Substituting this into Eq. (47), the entire residual term vanishes, and we recover
the multiplicative decomposition presented in the main text:
ρˆyδ,r∆ ≈ρ ˆyδ,rδ ·ρ rδ,r∆ .(48)
D.2. Proof of the Partial Correlation Formula
For completeness, we provide the step-by-step algebraic proof of the general formula used above.
1. Definition via Residuals.The partial correlation ρX,Y·Z between two random variables X and Y given a controlling
variableZis defined as the Pearson correlation between their residuals after linearly regressing outZ.
23

## PDF page 24

The Label Horizon Paradox: Rethinking Supervision Targets in Financial Forecasting
Without loss of generality, assume that X, Y , and Z are standardized variables with zero mean and unit variance (i.e.,
E[X] = 0,E[X 2] = 1). The linear regression ofXonZandYonZcan be expressed as:
ˆX=ρ X,Z Z, e X|Z =X− ˆX=X−ρ X,Z Z(49)
ˆY=ρ Y,Z Z, e Y|Z =Y− ˆY=Y−ρ Y,Z Z(50)
whereρ X,Z andρ Y,Z correspond to the regression coefficients (slopes) in the standardized case.
2. Deriving the Standard Formula.The partial correlation is the correlation of the residualse X|Z ande Y|Z :
ρX,Y·Z = E[eX|Z eY|Z ]q
E[e2
X|Z ]
q
E[e2
Y|Z ]
.(51)
Step 2.1: The Numerator (Covariance of Residuals).
E[eX|Z eY|Z ] =E[(X−ρ X,Z Z)(Y−ρ Y,Z Z)]\(52)
=E[XY−Xρ Y,Z Z−Y ρ X,Z Z+ρ X,Z ρY,Z Z2]\(53)
=E[XY]| {z }
ρX,Y
−ρY,Z E[XZ]| {z }
ρX,Z
−ρX,Z E[Y Z]| {z }
ρY,Z
+ρX,Z ρY,Z E[Z2]|{z}
1
(54)
=ρ X,Y −ρ X,Z ρY,Z −ρ X,Z ρY,Z +ρ X,Z ρY,Z (55)
=ρ X,Y −ρ X,Z ρY,Z .(56)
Step 2.2: The Denominator (Variance of Residuals).Since the residual variance is1−R 2:
E[e2
X|Z ] = 1−ρ 2
X,Z ,E[e 2
Y|Z ] = 1−ρ 2
Y,Z .(57)
Combining these, we recover the standard recursive formula:
ρX,Y·Z = ρX,Y −ρ X,Z ρY,Zq
1−ρ 2
X,Z
q
1−ρ 2
Y,Z
.(58)
3. Rearranging for the Decomposition Formula.We solve Eq. (58) for the total correlationρ X,Y :
ρX,Y·Z
q
1−ρ 2
X,Z
q
1−ρ 2
Y,Z =ρ X,Y −ρ X,Z ρY,Z (59)
ρX,Y =ρ X,Z ρY,Z +ρ X,Y·Z
q
1−ρ 2
X,Z
q
1−ρ 2
Y,Z .(60)
4. Application to the Label Horizon Problem.Finally, we substitute the variables from our main context ( X←ˆy δ,
Y←r ∆,Z←r δ) to obtain the formula in Eq. (47).
24

## PDF page 25

The Label Horizon Paradox: Rethinking Supervision Targets in Financial Forecasting
E. Supplementary Results
E.1. Results of Intraday Scenario
In the main text, we primarily focused on the standard interday prediction task (Scenario 1), which corresponds to the widely
used close-to-close setting in academic studies. To further assess the generality of our framework under different temporal
granularities, we report here the detailed experimental results for the two intraday scenarios defined in Section 3.1:
•Scenario 2:Intraday prediction with a 30-minute horizon (∆ = 30minutes).
•Scenario 3:Intraday prediction with a 90-minute horizon (∆ = 90minutes).
The experimental setup (data, feature construction, train/validation/test splits), the set of ten backbone architectures, and the
six evaluation metrics are kept identical to those used in Scenario 1 to ensure a fair comparison.
Tables 3 and 4 summarize the results for Scenario 2 and Scenario 3, respectively.
E.1.1. SCENARIO2 (30-MINUTE HORIZON)
From Table 3, we observe that our bi-level framework and the standard training baseline achieve very similar performance
across all three indices and all ten backbones. On most metrics, the two methods are within a narrow margin of each other,
and the winner alternates depending on the specific model–dataset combination.
This outcome is fully consistent with the empirical pattern observed in Figure 2. In Scenario 2, the performance curve as a
function of the training horizon is monotonically increasing, and the empirically optimal horizon δ∗ is essentially aligned
with the final target horizon ∆. Our bi-level procedure therefore learns to concentrate its weight near the target horizon,
effectively recovering the canonical choice. As a consequence, adaptively selecting the supervision horizon offers little
additional benefit over directly training on the final target, and the two approaches perform on par, with model-specific
fluctuations.
E.1.2. SCENARIO3 (90-MINUTE HORIZON)
For the longer intraday horizon in Scenario 3, Table 4 reveals a different picture. On many configurations, our method
achieves higher IC, RankIC, and Top Return than the standard baseline, indicating that adaptively shifting the supervision
away from the final horizon can indeed enhance the raw predictive signal. At the same time, there are a few exceptions
where the baseline slightly outperforms our method on these point-estimate metrics.
This mixed pattern is again aligned with the empirical phenomenon in Figure 2. In Scenario 3, the performance curve is
hump-shaped: the optimal horizon δ∗ lies somewhere between 0 and ∆, but the advantage of this intermediate horizon over
the final horizon is modest, and becomes visible mainly after Gaussian smoothing of the noisy empirical curve. In a realistic
high-noise financial environment, such a weak edge can be partially obscured by stochastic variability, so it is natural to see
some configurations where training directly on the final target remains competitive.
However, a more consistent advantage of our method emerges when we examine the stability metrics: ICIR, RankICIR, and
Sharpe Ratio. Across all three indices and most backbones in Scenario 3, our bi-level framework yields higher ICIR and
RankICIR than the standard baseline, and also improves the Sharpe Ratio in a largely uniform manner. This suggests that
even when the average IC gain is modest, adaptively selecting the supervision horizon helps the model produce signals that
are more stable over time and more robust to noise, which is crucial for practical portfolio construction.
E.2. Extended Analysis on the Necessity of Bi-level Optimization
In the main text, Section 6.1, we evaluate the necessity of bi-level optimization by comparing our method (training with
the selected best single label) against two label aggregation baselines: Naive Averaging (†) and Equal-Weight Multi-Task
Learning (‡). While our approach achieves the best overall performance, we observe that in Scenario 2 and Scenario 3, the
ICIR obtained from a single selected label is slightly lower than that of models trained on aggregated labels.
However, this comparison is inherently conservative with respect to our method, because training on a single horizon label
is naturally more volatile and statistically less stable than training on aggregated or multi-task targets that effectively average
out noise across multiple horizons. To provide a more fair comparison, we further leverage the information contained in the
25

## PDF page 26

The Label Horizon Paradox: Rethinking Supervision Targets in Financial Forecasting
Table 3.Results of Scenario 2.Comprehensive performance comparison between standard training (Std.) and our Bi-level framework
(Ours) across three market indices. All results are averaged over 5 random seeds. Bold indicates the better performance.
IC (×10) ICIR RANKIC (×10) RANKICIR TOPRET(%) SHARPERATIO
DATASETMODELSTD. OURSSTD. OURSSTD. OURSSTD. OURSSTD. OURSSTD. OURS
CSI 300
LSTM 1.2231.243 0.7450.716 1.5581.604 1.2101.184 0.0740.0743.5123.715
GRU 1.1951.225 0.7230.690 1.6661.693 1.1441.107 0.0780.0803.9004.106
DLINEAR1.2081.183 0.6890.722 1.6121.592 1.1971.2580.0720.075 3.9513.799
RLINEAR1.1941.1930.8190.786 1.5191.536 1.2181.158 0.0710.0743.5473.739
PATCHTST 1.1761.2810.8350.8551.4341.6301.2021.3110.0700.0783.8323.995
ITRANSFORMER1.2791.239 0.8110.855 1.6411.5711.3461.323 0.0760.0783.9103.936
MAMBA1.2681.259 0.8230.8441.6161.6581.2971.3280.0790.0843.8124.552
BI-MAMBA+1.2421.220 0.8510.855 1.5911.5361.3031.2990.0820.0724.3323.623
MODERNTCN1.2511.2340.7160.7071.5831.5211.2561.2350.0760.0723.9953.950
TCN 1.2291.240 0.7290.691 1.5971.605 1.2541.238 0.0790.0844.1104.123
CSI 500
LSTM 1.4741.4911.3721.3961.9221.9431.9312.0620.1210.122 5.1725.076
GRU 1.5081.5151.3341.347 1.9781.946 2.0412.094 0.1270.126 5.2905.325
DLINEAR1.5141.5041.4171.394 1.9151.933 2.1111.9250.1270.1215.3505.122
RLINEAR1.4681.496 1.3811.345 1.8811.9322.0242.096 0.1270.1265.2785.163
PATCHTST1.4981.4701.4711.3081.9561.9252.1801.970 0.1270.1285.3015.391
ITRANSFORMER1.4721.4801.2461.372 1.9501.947 1.9402.0320.1180.120 5.1885.051
MAMBA1.5141.5121.3941.346 1.9471.956 2.0342.0070.1260.1245.3175.260
BI-MAMBA+1.5261.477 1.3051.372 2.0141.892 1.9732.064 0.1310.1235.6465.005
MODERNTCN 1.4811.4721.3391.3591.9051.9331.9301.9780.1240.1265.1735.228
TCN1.5331.5161.3941.3671.9541.9202.1022.021 0.1280.1315.3105.373
CSI 1000
LSTM1.1611.1561.1001.0661.9101.8521.8891.8730.1150.1144.4183.908
GRU1.1661.1601.1411.052 1.8391.898 1.9831.935 0.1080.1144.0424.481
DLINEAR1.1671.189 1.1381.112 1.8041.8881.8281.8400.1080.1144.0704.317
RLINEAR1.1811.1651.1701.066 1.8631.933 1.9411.881 0.1090.1144.1404.464
PATCHTST 1.1441.1461.1071.1131.7811.8731.7551.9120.1090.1153.8134.496
ITRANSFORMER1.2031.170 1.1111.143 1.9141.8271.8651.856 0.1130.114 4.4654.251
MAMBA1.1821.1881.0391.085 1.9611.945 1.8091.9320.1100.1154.3014.427
BI-MAMBA+ 1.1871.1871.0731.145 1.9581.855 1.8221.978 0.1140.1104.4884.098
MODERNTCN 1.1471.178 1.1271.098 1.6941.8441.8511.9560.1070.1123.9604.187
TCN 1.2101.2251.0591.232 1.9471.825 1.8311.998 0.1150.1114.4684.153
learned horizon weightsλ:
• We first identify the top-5horizons with the largest weights inλ.
• Using only these top-5selected horizons, we then construct:
1. A Naive Averaging variant (∗ †): train a model on the arithmetic mean of these top-5labels.
2. An Equal-Weight MTL variant (∗ ‡): train a model using only these top- 5 horizons with equal weights in the
multi-task loss.
In other words, we retain our bi-level optimization to select informative horizons, but then train baselines that aggregate or
jointly model only these selected labels, instead of all candidates. This design removes the unfair advantage of aggregating
over many noisy horizons, while still allowing label smoothing through averaging or multi-task learning.
Table 5 reports the performance of these additional configurations, again using an LSTM backbone on CSI 500 under
Scenarios 1, 2, and 3. The results show that, once we restrict baselines to the top- 5 horizons identified by our bi-level
procedure, the resulting models consistently outperform their counterparts trained on all horizons.
E.3. Generalization to US Markets (S&P 500)
To confirm that our proposed framework represents a general supervision principle rather than an artifact of a specific
market, we extend our evaluation to the US equity market. Specifically, we conduct new experiments on the S&P 500 index.
This evaluation strictly follows the Scenario 1 (daily prediction) protocol from the main paper, including data structure,
feature engineering, and label construction. The dataset is chronologically split into January 2019–July 2023 (Train), July
2023–July 2024 (Validation), and July 2024–July 2025 (Test). The only adjustment made is a longer input sequence to
accommodate the longer daily trading session characteristic of the US market.
26

## PDF page 27

The Label Horizon Paradox: Rethinking Supervision Targets in Financial Forecasting
Table 4.Results of Scenario 3.Comprehensive performance comparison between standard training (Std.) and our Bi-level framework
(Ours) across three market indices. All results are averaged over 5 random seeds. Bold indicates the better performance.
IC (×10) ICIR RANKIC (×10) RANKICIR TOPRET(%) SHARPERATIO
DATASETMODELSTD. OURSSTD. OURSSTD. OURSSTD. OURSSTD. OURSSTD. OURS
CSI 300
LSTM 0.9370.9470.5300.666 1.2451.136 0.8861.0100.0390.0461.1141.240
GRU 0.9280.9340.5600.5781.2281.2410.8910.9360.0290.0490.8431.421
DLINEAR0.8650.834 0.5110.669 1.1441.087 0.9331.0020.0270.0550.7601.635
RLINEAR0.8770.9040.6320.6551.1171.1910.9591.0200.0380.0411.0161.137
PATCHTST 0.8670.9760.6360.6711.0021.2160.8521.0070.0330.0440.9531.287
ITRANSFORMER0.8910.9500.5930.6391.1621.1751.0031.0460.0420.0611.1671.785
MAMBA0.9491.0430.6340.6691.1441.3080.9671.0810.0430.0591.2161.769
BI-MAMBA+ 0.9661.0580.6050.6551.2251.2830.9700.9800.0470.0611.3171.823
MODERNTCN 0.9501.0590.5170.5431.2101.4070.8090.8620.0330.0551.0311.790
TCN 0.8561.002 0.6250.556 1.0021.317 0.9660.933 0.0310.0530.8831.630
CSI 500
LSTM 1.0691.0821.0191.095 1.4071.399 1.5631.609 0.0830.0802.0961.809
GRU 1.0521.0801.0161.2211.4141.4351.4991.6940.0740.0811.6611.923
DLINEAR1.0380.991 1.0221.064 1.2771.2411.5251.458 0.0720.0781.6581.889
RLINEAR0.9351.0231.0991.2281.1531.2831.4591.5900.0680.0791.4941.772
PATCHTST1.0471.036 0.9751.232 1.3971.306 1.4421.6570.0860.0911.9751.999
ITRANSFORMER1.0721.039 1.1191.233 1.3871.344 1.6391.7330.0850.0922.0442.069
MAMBA1.0831.1081.0561.2091.3971.4051.5541.6700.0810.0861.8771.952
BI-MAMBA+ 1.0751.1001.0531.2221.3311.4311.5481.6460.0780.0891.7252.103
MODERNTCN 0.9961.0270.9861.0241.1761.4071.5371.6590.0740.0801.9182.069
TCN 1.0811.1051.0471.1781.3281.3811.5161.6570.0780.0921.7652.141
CSI 1000
LSTM 0.8840.9280.8501.0121.2441.4471.5501.5530.0760.0761.5141.631
GRU 0.9030.9070.8881.069 1.3891.333 1.6051.6510.0680.0801.4041.675
DLINEAR0.9240.891 0.8731.136 1.3851.310 1.4771.635 0.0750.0671.6471.609
RLINEAR0.8610.9060.9750.9981.2251.3211.4941.5740.0620.0741.2571.537
PATCHTST 0.8990.924 0.9950.967 1.2361.3661.5901.5990.0650.0831.3101.737
ITRANSFORMER0.9480.942 0.9291.029 1.3181.311 1.5501.6200.0740.0771.5571.627
MAMBA0.8940.9080.9091.0581.3091.3331.5771.7650.0700.0781.4691.610
BI-MAMBA+0.9550.931 0.8980.962 1.4401.3461.6571.5960.0850.0831.8771.719
MODERNTCN 0.9160.9410.8720.9791.3111.3741.5151.5290.0740.0781.5031.718
TCN 0.9320.9510.9601.0481.3041.3271.5691.6300.0740.0831.5391.711
The US market is widely recognized as highly efficient, meaning that information is absorbed into prices much faster than in
emerging markets. According to our theoretical framework (Section 3.2), a faster signal realization rate (α′(δ)→0 earlier)
implies a more rapid dominance of the noise penalty, leading to a faster performance decay over the prediction horizon.
As shown in Table 6, our bi-level framework consistently outperforms the standard paradigm across all ten backbone
architectures. This confirms that the Label Horizon Paradox exists even in highly efficient markets, and our adaptive horizon
learning effectively navigates the rapid signal-noise trade-off inherent in the US market.
E.4. Stress Tests During Market Crashes
To further evaluate the risk resilience and temporal generalizability of our framework, we conducted a stress test focusing on
a period of extreme market volatility. Specifically, we evaluate our models on the CSI 500 index with a shifted timeframe
to capture a period of severe and continuous macroeconomic downtrend, culminating in the well-known market crash in
February 2024.
Similar to the US market evaluation, this stress test strictly follows the Scenario 1 protocol regarding data structure, feature
engineering, and label construction. The dataset is chronologically split into January 2018–July 2022 (Train), July 2022–July
2023 (Validation), and July 2023–July 2024 (Test, which covers the aforementioned market crash).
As shown in Table 7, despite the extreme market stress and distribution shifts, models trained with our bi-level optimization
framework consistently maintain their performance improvements over the standard baselines. This robust performance
demonstrates that dynamic label selection not only enhances signal quality in normal market conditions but also provides
crucial stability when the market undergoes severe structural shocks.
27

## PDF page 28

The Label Horizon Paradox: Rethinking Supervision Targets in Financial Forecasting
Table 5.Impact of Horizon Selection on Aggregation and MTL Performance.Experiments are conducted using an LSTM backbone
across Scenarios 1, 2, and 3 on CSI 500. We compare: (i) training with all candidate horizons (Naive Averaging: †; Equal-Weight MTL:
‡), and (ii) training with only the top-5 horizons selected by the learned horizon weights λ (Naive Averaging on top-5: ∗†; Equal-Weight
MTL on top-5: ∗‡). The results show that using the bi-level-selected top-5horizons consistently improves over using all horizons.
CONFIGURATIONIC(×10) ICIR RANKIC(×10) RANKICIR TOPRET(%) SHARPERATIO
SCENARIO1 ∗ 1.029 0.861 0.859 0.895 0.383 3.660
SCENARIO1 † 0.969 0.778 0.821 0.817 0.374 3.516
SCENARIO1 ∗ † 1.066 0.865 0.902 0.921 0.398 3.682
SCENARIO1 ‡ 0.932 0.803 0.814 0.837 0.380 3.377
SCENARIO1 ∗ ‡ 0.973 0.821 0.860 0.842 0.377 3.420
SCENARIO2 ∗ 1.4911.3961.9432.062 0.122 5.076
SCENARIO2 † 1.453 1.471 1.857 2.021 0.121 4.933
SCENARIO2 ∗ † 1.486 1.6131.8922.104 0.1265.089
SCENARIO2 ‡ 1.435 1.456 1.849 1.998 0.123 4.931
SCENARIO2 ∗ ‡ 1.483 1.479 1.935 2.097 0.124 5.095
SCENARIO3 ∗ 1.082 1.095 1.399 1.609 0.080 1.809
SCENARIO3 † 1.050 1.125 1.359 1.538 0.082 1.935
SCENARIO3 ∗ † 1.086 1.247 1.4641.642 0.087 2.073
SCENARIO3 ‡ 1.071 1.118 1.367 1.596 0.085 1.965
SCENARIO3 ∗ ‡ 1.083 1.181 1.448 1.6690.085 1.975
Table 6.Results on the US Market (S&P 500).Comprehensive performance comparison under the daily prediction setting. All results
are averaged over 5 random seeds. Bold indicates the better performance.
IC (×10) ICIR RANKIC (×10) RANKICIR TOPRET(%) SHARPERATIO
DATASETMODELSTD. OURSSTD. OURSSTD. OURSSTD. OURSSTD. OURSSTD. OURS
S&P 500
LSTM 0.3140.4590.3020.4410.1490.2190.1390.2060.1410.1591.4431.600
GRU 0.3460.3990.3330.3510.1810.2020.1810.184 0.1640.157 1.5601.618
DLINEAR0.3260.5060.3320.4720.1390.2130.1590.2150.1250.1661.3681.733
RLINEAR0.3520.4610.3350.4520.1700.1990.1710.2140.1550.1591.5441.614
PATCHTST 0.3090.4890.3470.421 0.1800.178 0.1690.2160.1370.1481.3301.570
ITRANSFORMER0.3970.4990.4020.4350.2150.2280.1870.232 0.1770.175 1.7122.097
MAMBA0.4290.5270.4060.5390.1920.2410.1800.2450.1600.1751.6401.875
BI-MAMBA+ 0.3150.4730.2360.4170.1770.2250.1240.1820.1490.1641.4091.653
MODERNTCN 0.3060.4550.2470.3830.1410.1980.1110.1710.1360.1551.2311.486
TCN 0.4230.5400.3880.5150.2000.2500.2100.2270.1640.1681.6771.686
E.5. Downstream Portfolio Backtesting
To further demonstrate the practical application value of our framework, we extend our evaluation beyond statistical
predictive metrics by conducting a simple downstream portfolio backtesting experiment. This simulation incorporates
realistic trading constraints to assess the actual economic value generated by the predictive signals.
Experimental Setup.Following standard quantitative investment paradigms, we construct a daily rebalanced, equal-weight
portfolio. The detailed settings are as follows:
• Stock Universe & Period:The backtest is conducted on the constituents of the CSI 500 index over the test period
from July 2024 to July 2025.
• Execution Strategy:To prevent look-ahead bias and simulate realistic execution, the models generate predictions 15
minutes before the market close. We then use the Time-Weighted Average Price (TW AP) of the subsequent 10 minutes
as the execution price for all trades.
• Portfolio Construction:On each trading day, we select the top 20% of stocks with the highest predicted scores and
assign them equal weights in the portfolio.
28

## PDF page 29

The Label Horizon Paradox: Rethinking Supervision Targets in Financial Forecasting
Table 7.Stress Test Results on CSI 500 (Jul 2023 – Jul 2024).Performance comparison during a severe market downtrend and crash.
All results are averaged over 5 random seeds. Bold indicates the better performance.
IC (×10) ICIR RANKIC (×10) RANKICIR TOPRET(%) SHARPERATIO
DATASETMODELSTD. OURSSTD. OURSSTD. OURSSTD. OURSSTD. OURSSTD. OURS
CSI 500
LSTM 0.8740.909 0.9270.916 0.8170.9321.0131.1040.1290.1311.4111.454
GRU 0.8830.8900.8870.9280.8430.9261.0161.0530.1230.129 1.4141.341
DLINEAR0.7460.8170.8010.8170.7490.8650.9141.0150.1030.1251.1641.362
RLINEAR0.8790.8840.9210.9790.8970.924 1.1171.0860.1300.126 1.3671.458
PATCHTST 0.8840.9310.8570.8610.8620.9740.9281.0050.1280.1361.3871.469
ITRANSFORMER0.8460.9100.8280.8680.8710.9460.9851.0320.1060.1291.1761.438
MAMBA0.9220.9650.9270.9820.9151.0111.0551.0830.1260.1391.4021.511
BI-MAMBA+ 0.9530.957 0.9300.906 0.8960.9900.9771.0690.1380.1411.4951.542
MODERNTCN 0.7400.8470.7440.8230.6980.8680.7620.9290.0890.1190.9811.319
TCN 0.9350.9510.9400.9780.9290.9641.0491.0970.1290.1341.3971.451
• Real-world Constraints:Transaction costs (commissions and stamp duties) and execution slippage are strictly
incorporated into the backtesting framework to accurately reflect real-world trading frictions.
As shown in Table 8, applying our bi-level optimization method consistently improves downstream trading performance
across almost all backbone architectures. Notably, our framework not only enhances the Annualized Return (Ann. Ret) but
also effectively reduces the Maximum Drawdown (MDD) and Annualized V olatility (Ann. V ol) in most cases. Consequently,
the risk-adjusted returns, measured by the Sharpe Ratio, exhibit substantial and consistent improvements over the standard
training paradigm.
Table 8.Downstream Portfolio Backtesting Results on CSI 500.Performance comparison incorporating real-world constraints such as
transaction costs and TW AP execution. Bold indicates the better performance.
ANN. RET(%) ANN. VOL(%) SHARPERATIOMDD (%)
DATASETMODELSTD. OURSSTD. OURSSTD. OURSSTD. OURS
CSI 500
LSTM 42.1842.2725.8924.531.631.72-13.96-11.25
GRU 36.1540.9025.0124.681.451.66-13.55-12.17
DLINEAR34.4141.6525.1124.801.371.68-12.84-12.01
RLINEAR33.9741.04 23.8724.95 1.421.64-12.56-11.85
PATCHTST 38.5945.8025.6924.761.501.85-13.37-12.48
ITRANSFORMER34.9537.68 24.4724.82 1.431.52-12.70-11.56
MAMBA38.1946.4624.7224.651.551.88-12.17-12.10
BI-MAMBA+39.4039.17 25.9624.131.521.62-12.28-11.88
MODERNTCN 29.5633.8824.7324.211.201.40-13.24-12.67
TCN 33.1440.22 24.85 24.851.331.62-13.88-11.67
29

## PDF page 30

The Label Horizon Paradox: Rethinking Supervision Targets in Financial Forecasting
F. Efficiency Analysis
In this section, we provide an empirical efficiency analysis of the proposed bi-level optimization framework. Following
the main experimental setup, we benchmark the per-epoch training time of a standard predictive model against its bi-level
counterpart under Scenario 1 on the CSI 1000 universe, using a single NVIDIA H20 GPU.
We choose CSI 1000 for this analysis because it is the largest universe considered in our experiments, thus presenting the
heaviest computational load. Consequently, any additional overhead introduced by the bi-level procedure would be most
evident in this setting.
We report results for a diverse set of sequence and time-series architectures. For each model, we measure the time required
to complete a single training epoch under:
1.Standard training: conventional supervised learning without bi-level optimization.
2.Bi-level training: our proposed method with a single-step inner loop update.
The measured per-epoch training times on the CSI 1000 dataset are summarized in Table 9. The results show that, with a
single inner-loop step, the bi-level method adds a moderate amount of computational overhead compared with standard
training, and remains practically implementable across all tested architectures. This is particularly natural in quantitative
finance, where the signal-to-noise ratio is typically low and models tend to use relatively modest parameter sizes to control
overfitting. Under such model sizes, the extra computation required by the inner update is contained, and the overall training
cost stays in a comparable range to that of standard supervised training.
We note that in other application domains with substantially larger models or more complex architectures, the relative
overhead of bi-level optimization could be higher. However, within our forecasting task and model configurations, the
impact on efficiency is not significant. At the same time, the bi-level approach effectively avoids the need for extensive
repeated training runs for horizon selection, which would otherwise involve training tens or hundreds of separate models,
leading to much higher total computational cost.
It is also important to emphasize that the absolute per-epoch times across different models in Table 9 are not meant to be
directly compared as indicators of model quality or efficiency. The models have different architectures and parameter counts:
for instance, Transformer-based models are, in principle, more computationally intensive than RNN-based models. Yet in
practice, Transformer models in financial forecasting often need to be kept relatively small to mitigate overfitting, which can
narrow the gap in actual runtime compared with lighter architectures. Therefore, the primary takeaway from this analysis is
the relative overhead of bi-level training versus standard training for each given model, rather than cross-model runtime
comparisons.
Table 9.Comparison of Running Time.Per-epoch training time (in seconds) on CSI 1000 under Scenario 1 using a single NVIDIA
H20 GPU. Standard Training denotes conventional supervised training without bi-level optimization, while Bi-level Training denotes
our method with a single inner-loop update per outer iteration. CSI 1000 is chosen as it corresponds to the largest universe and thus the
heaviest computational load.
MODELSTANDARDTRAINING(S/EPOCH) BI-LEVELTRAINING(S/EPOCH)
LSTM 21.739 22.137
GRU 21.825 22.536
DLINEAR21.568 22.672
RLINEAR21.357 22.912
PATCHTST 21.653 23.357
ITRANSFORMER21.153 23.540
MAMBA21.912 25.688
BI-MAMBA+ 21.401 27.765
MODERNTCN 21.317 26.583
TCN 21.484 23.284
30
