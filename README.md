# Booth-Algorithm

Booth’s algorithm is an efficient method to multiply two signed binary numbers. The method requires a multiplier `Q (n bits)`, a multiplicand `M (n bits)`, a register `A (2n bits)`, and an additional register `Q-1 (1 bit)`. The `2n-bits` register and the `1-bit` register are initially initialized to zero. During the calculation, `Q-1` stores the last bit of `Q` in the previous step, and additions and subtractions are performed over `A`.

The following are the three conditions needed for calculating the correct result.
* If `Q0 Q-1` is equal to `10`, then perform `A = A – M` and the right shift.
* If `Q0 Q-1` is equal to `01`, then perform `A = A + M` and the right shift.
* If` Q0 Q-1` is equal to `11`, or `00`, then just perform the right shift.

## Constraints and Assumptions
* The value of `n` (number of bits) considered in the program is `10`. 
* The Multiplier and the Multiplicand should be strictly in the range `(-512, 512)`. 
* The product obtained will be of `20 bits (2n)`.
