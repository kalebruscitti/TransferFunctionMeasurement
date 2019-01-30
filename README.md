# TransferFunctionMeasurement
Code and files for a project at IQC under Raffi Budakian, to measure the electrical transfer function of the experiment

How to use:

The Main.vi file is the VI that should be used to collect data. The reference signal at the specified cantilever frequency will be ouput from the first channel of the AWG. The second channel will output a signal of the form $$A_1 \sin(2*\pi*f_0 t + A_2 \sin(2*\pi*(f_0 + f_c) t)$$

