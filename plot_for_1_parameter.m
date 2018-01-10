clear;
clc;

fname = 'exout2.csv'

M = csvread(fname,1);
fid = fopen(fname);
Ids = textscan(fid,'%s %s',1);%Number of elements in the header
fclose(fid);


f = M(:,1);
y1 = M(:,2);


p = plot(f,y1);

p(1).LineWidth = 1.5;
p(1).LineStyle = '-';
% p(1).Marker = 's';
% p(1).MarkerIndices = 1:11:length(f);
p(1).Color = 'k';

xlabel('Frequency (GHz)');
ylabel('S parameters (dB)');

legend(Ids{2}{1},'Location','southeast');
legend('boxoff')

set(gca, 'FontName', 'Times New Roman')
set(gca, 'FontSize', 14)

