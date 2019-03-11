# TransferFunctionMeasurement
Code and files for a project at IQC under Raffi Budakian, to measure the electrical transfer function of the experiment

How to use:

The Main.vi file is the VI that should be used to collect data. The reference signal at the specified cantilever frequency will be ouput from the first channel of the AWG. The second channel will output a signal of the form A_1 sin(2*\pi*f_0 t) + A_2 sin(2*\pi*(f_0 + f_c) t)

Relative phase and amplitude are controlled in the main vi. If you want to control the settings on the AWG or lock-in amplifier, use initalize_devices.vi. If you select 'Write Settings to File' then these settings will be output to a textfile so you can reproduce the same data again later.

If you want to apply an external transfer function to your device, you need to generate a transfer function CSV file with the Generate Transfer Function script. There is a GUI for this script included (executable binary can be downloaded from releases). The frequency range and steps must match those desired for your scan. Then you can select this file in the main VI and the transfer function will be applied to your output signal.
