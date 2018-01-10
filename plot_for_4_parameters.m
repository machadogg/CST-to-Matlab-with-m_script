clear;
clc;

fname = 'exout4.csv'

M = csvread(fname,1);
fid = fopen(fname);
Ids = textscan(fid,'%s %s %s %s %s %s %s %s',1);%Number of elements in the header
fclose(fid);


f = M(:,1);
y1 = M(:,2);
y2 = M(:,4);
y3 = M(:,6);
y4 = M(:,8);

p = plot(f,y1,f,y2,f,y3,f,y4);

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

p(4).LineWidth = 1.5;
p(4).LineStyle = '-.';
% p(4).Marker = 'd';
% p(4).MarkerIndices = 1:71:length(f);
p(4).Color = 'k';

xlabel('Frequency (GHz)');
ylabel('S parameters (dB)');

% legend('S_{11} TE','S_{11} TM', 'S_{21} TE','Location','southeast')
legend(Ids{2}{1},Ids{4}{1},Ids{6}{1},Ids{8}{1},'Location','southeast');
legend('boxoff')

set(gca, 'FontName', 'Times New Roman')
set(gca, 'FontSize', 14)

