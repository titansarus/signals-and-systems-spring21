clean1 =audioread("clean1.wav");
f_clean1=fft(clean1);
distorted1 = audioread("distorted1.wav");
f_distort1 = fft(distorted1);

h_inv = f_clean1./f_distort1;

distort2 = audioread("distorted2.wav");
f_dsitort2 = fft(distort2);

f_clean2 = h_inv .* f_dsitort2;
