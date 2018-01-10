clear;
clc;

fname = 'exout2.csv'

M = csvread(fname,1);
fid = fopen(fname);
Ids = textscan(fid,'%s %s %s %s',1);%Number of elements in the header
fclose(fid);


f = M(:,1);
y1 = M(:,2);
y2 = M(:,4);


p = plot(f,y1,f,y2);

p(1).LineWidth = 1.5;
p(1).LineStyle = '-';
% p(1).Marker = 's';
% p(1).MarkerIndices = 1:11:length(f);
p(1).Color = 'k';

p(2).LineWidth = 2;
p(2).LineStyle = '--';
% p(2).Marker = 'o';
% p(2).MarkerIndices = 1:51:length(f);
p(2).Color = 'k';

xlabel('Frequency (GHz)');
ylabel('S parameters (dB)');

legend(Ids{2}{1},Ids{4}{1},'Location','southeast');
legend('boxoff')

set(gca, 'FontName', 'Times New Roman')
set(gca, 'FontSize', 14)

