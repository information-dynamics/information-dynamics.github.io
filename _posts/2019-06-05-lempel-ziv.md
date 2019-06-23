---
layout: post
title:  "When and how to use Lempel-Ziv complexity"
date:   2019-06-05 19:54:09 +0100
author: Fernando Rosas and Pedro Mediano
categories: complexity information
description: 'The Lempel-Ziv complexity (LZ) is a popular tool to quantify the uncertainty
contained in time series data. In particular, LZ measures how "diverse"
are the patterns that are present in a particular signal.'
---



The Lempel-Ziv complexity (LZ) is a popular tool to quantify the uncertainty
contained in time series data. In particular, LZ measures how "diverse"
are the patterns that are present in a particular signal. 

The LZ method was introduced back in 1976 by the electrical engineers Abraham
Lempel and Jacob Ziv to study binary sequences [[Lempel1976](#Lempel1976)].
These core ideas were later extended
[[Ziv1977](#Ziv1977),[Ziv1978a](#Ziv1978a)] to become the basis of the
well-known `zip` compression algorithm, which is used every day by millions of
people to compress files. In parallel, this algorithm has been used by
scientists to study the diversity of patterns in signals of diverse nature. In
particular, studies on EEG brain activity have been carried out using LZ for
more than 20 years, with some early studies focusing on epilepsy
[[Radhakrishnan1998](#Radhakrishnan1998)] and depth of anaesthesia
[[Zhang2001](#Zhang2001)], and more modern ones on other altered states of
consciousness [[Schartner2017](#Schartner2017)]. Outside neuroscience, LZ has
also been used to study the complexity of DNA sequences
[[Gusev1999](#Gusev1999)] and ventricular fibrillation
[[Zhang1999](#Zhang1999)], and has become a well-established tool for
biomedical data analysis [[Aboy2006](#Aboy2006)].

<!--In recent years LZ has been established as one of the preferred tools to study 
altered states of consciousness from EEG signals. This trend goes back to the
"Entropic Brain Hypothesis", which proposes that richness of psychological
content is correlated with richness (diversity) of brain signal. In simple words,
special psychological states should not be found in more or less activity of a
specific kind (e.g. alpha, beta, or other waves), but in more diverse activity.
The LZ has been positioned as the favourite method to quantify signal
diversity, both because of it simple implementation, than for it robustness 
of it results.-->

LZ is calculated in two steps. First, the value of a given signal $$X$$ of length
$$T$$ is binarised. The standard way of doing this is calculating its mean value 
and turning each data point above it to `1`s and each point below it to `0`s;
however, other possibilities have also been used (thresholding over the median, using the Hilbert transform, etc...).
As a second step, the resulting binary sequence is scanned sequentially looking for distinct 
structures or *patterns*, building up a dictionary that summarises 
the sequences seen so far. Finally, the LZ index is determined by
the length of this dictionary; i.e., is the number of
distinct patterns found, denoted by $$C(X)$$. Note that regular signals can be
characterized by a small number of patterns and hence have low LZ complexity,
while irregular signals require long dictionaries and hence have a high LZ
complexity.

Following the reasoning above, the LZ method identifies signal complexity with
*richness of content* [[Mitchell2009](#Mitchell2009)]. In this way, a signal is regarded as
complex if it is not possible to provide a brief (i.e. compressed)
representation of it. 

A popular way of making sense of LZ is by considering
a proxy for estimating the value of the Kolmogorov complexity, which is the length of the shortest
computer program that reproduce a given pattern [[Vitanyi1997](#Vitanyi1997)]. However, we
argue that this view is brittle in theory and of limited use in
practice. As a matter of fact, the comparison between the Kolmogorov complexities of finite
strings is highly problematic [[Cover2006](#Cover2006)]. The Kolmogorov complexity of a finite string differs by an additive constant depending on the Turing machine used to compress it. The problem is that for finite 
of *any* length the magnitude of this constant is unbounded, making
comparisons between Kolmogorov complexities estimated from finite data
essentially meaningless.

A simpler and more straightforward interpretation of LZ is by to focus on the quantity

$$
\begin{equation*}
c(X) := \frac{T}{\log(T)} C(X)  
\end{equation*}
$$

which is known to be an efficient estimator of the **entropy rate** of $$X$$ [[Ziv1978b](#Ziv1978b)]. 
The entropy rate is a quantity from Information Theory, which measures how many bits of 
innovation are introduced by each new data sample [[Cover2006](#Cover2006)]. Moreover, the entropy
rate is a good measure of how hard it is to predict the next value of a sequence. 
In effect, one half of the entropy rate approximates the probability of making an error with the best
informed guess about the next sample [[Feder1994](#Feder1994)]. Note that while LZ can 
-- strictly speaking -- be applied to non-stationary data, 
the interpretation as entropy rate assumes that the data is stationary.

The previous interpretation is valid to the so called LZ76, which was defined in Ref.[REF].
There are two other versions of the LZ algorithm, known as LZ77 and LZ78 according to the
year in which they were published. The numerical value of LZ differs when computed
by the different versions; however, by using appropriate scaling any of these can be
made to converge to the entropy rate of the process. However, in our experience LZ76 converge
faster than LZ77 and LZ78, and also it computational time is much faster.

### References

<a name="Schartner2017"></a>Schartner, M. M., Carhart-Harris, R. L., Barrett, A. B., Seth,
A. K., & Muthukumaraswamy, S. D. (2017). Increased spontaneous MEG signal
diversity for psychoactive doses of ketamine, LSD and psilocybin. Scientific
Reports, 7, 46421.

