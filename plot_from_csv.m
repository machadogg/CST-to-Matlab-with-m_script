clear;
clc;

M = csvread('z2.csv',1);
fid = fopen('z2.csv');
Ids = textscan(fid,'%s %s %s %s %s %s',1);%Number of elements in the header
fclose(fid);


f = M(:,1);
s11te = M(:,2);
s11tm = M(:,4);
s21te = M(:,6);

p = plot(f,s11te,f,s11tm,f,s21te);

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

p(3).LineWidth = 1.5;
p(3).LineStyle = ':';
% p(3).Marker = 'd';
% p(3).MarkerIndices = 1:71:length(f);
p(3).Color = 'k';

xlabel('Frequency (GHz)');
ylabel('S parameters (dB)');

% legend('S_{11} TE','S_{11} TM', 'S_{21} TE','Location','southeast')
legend(Ids{2}{1},Ids{4}{1},Ids{6}{1},'Location','southeast');
legend('boxoff')

set(gca, 'FontName', 'Times New Roman')
set(gca, 'FontSize', 14)

