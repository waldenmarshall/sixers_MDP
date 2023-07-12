function [t,N] = create_hist_data(x)
%UNTITLED Summary of this function goes here
%   Detailed explanation goes here

nbins=1+max(x)-min(x);
t=[min(x):max(x)]';
N=zeros(nbins,1);

for i=1:length(x)
    j=x(i)+1-min(x);
    N(j)=N(j)+1;
end

%histogramdata=[t;N];

end
