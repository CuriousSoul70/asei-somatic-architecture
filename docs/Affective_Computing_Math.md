# Biometric Vectorization & The Circumplex Model

The ASEI Edge Broker interprets raw physiological telemetry by mapping it to Russell's Circumplex Model of Affect (Valence vs. Arousal)[cite: 2]. 

## 1. Arousal Vector ($A$)
Arousal is quantified via sympathetic nervous system activity, primarily driven by Electrodermal Activity (EDA)[cite: 2]. The system calculates shifts in tonic Skin Conductance Level (SCL) and the frequency of phasic Skin Conductance Responses (SCR)[cite: 2].

$$A = \tanh\left(\alpha \cdot \Delta \text{SCL} + \beta \cdot \text{SCR}_{\text{freq}}\right)$$

## 2. Valence Vector ($V$)
Valence (emotional positivity/negativity) is derived from parasympathetic vagal tone, measured via Heart Rate Variability (HRV)[cite: 2]. The engine uses the Root Mean Square of Successive Differences (RMSSD) and the frequency domain ratio of Low Frequency (LF) to High Frequency (HF) power[cite: 2].

$$V = \tanh\left(\gamma \cdot \frac{\text{RMSSD} - \mu_{\text{RMSSD}}}{\sigma_{\text{RMSSD}}} - \delta \cdot \frac{\text{LF}}{\text{HF}}\right)$$
