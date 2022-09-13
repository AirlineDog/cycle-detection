# cycle-detection

If we have a sequence of numbers produced by a function, how can we know that the generated values are not repeated? Or, if reoccurring, when does this start happening?


This repo implements the algorithms described in the article below:


Sedgewick, Robert, Thomas G. Szymanski, and Andrew C. Yao. 1982. “The Complexity
of Finding Cycles in Periodic Functions.” SIAM Journal on Computing 11 (2): 376–
90. https://doi.org/10.1137/0211030.

https://github.com/AirlineDog/cycle-detection/blob/0d117aabf2fd716865b85e324ccf27ee57b9693d/cycle_detection.py#L31-L48

The basic idea behind this algorithm is that instead of examining all values of the sequence, we only examine *b* values, which are within *gb* of each other, where *b*, *g* are parameters that we have to choose. Those values are stored in a table containing pairs *(y, j)*, where *y* is a value of the sequence and *j* the order we found it. For every *y* the table can have more than one corresponding *j*.

The algorithm stores values in the table in order not to recalculate them. If a sequence is too long this can result in a very big table. To avoid that we put a *max_size* limit to the table. When the table is full we purge all pairs that `j mod 2b != 0` and we double the parameter *b*


The next step is to find where this cycle is starting, that is the *leader*, and how long the cycle is.

https://github.com/AirlineDog/cycle-detection/blob/0d117aabf2fd716865b85e324ccf27ee57b9693d/cycle_detection.py#L51-L71

