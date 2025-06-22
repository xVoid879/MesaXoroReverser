# MesaXoroReverser
Generates two consecutive nextLong outputs from the internal Xoroshiro128++ RNG state with a given Minecraft 64-bit world seed. This simulates the Mesa Bands random sequence. You can then reverse these two outputs to recover the full 128-bit internal RNG state.


**Current Observed Data**
Using seed: -8734629182736458273
First nextLong(): 0x4AB8CC5FDCFBA9B9
Second nextLong(): 0x31AD69B0BB802D45

I'm currently using an SMT solver to use these consecutive nextLong() to obtain the full 128 bit internal state.
