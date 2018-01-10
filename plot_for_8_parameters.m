clear;
clc;

fname = 'file_name.csv'

M = csvread(fname,1);
fid = fopen(fname);
Ids = textscan(fid,'%s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s',1);%Number of elements in the header
fclose(fid);


f = M(:,1);
y1 = M(:,2);
y2 = M(:,4);
y3 = M(:,6);
y4 = M(:,8);
y5 = M(:,10);
y6 = M(:,12);
y7 = M(:,14);
y8 = M(:,16);

p = plot(f,y1,f,y2,f,y3,f,y4,f,y5,f,y6,f,y7,f,y8);

p(1).LineWidth = 1.5;
p(1).LineStyle = '-';
% p(1).Marker = 's';
% p(1).MarkerIndices = 1:11:length(f);
p(1).Color = [0.8471 0.3216 0.0941];

p(2).LineWidth = 2;
p(2).LineStyle = '--';
% p(2).Marker = 'o';
% p(2).MarkerIndices = 1:51:length(f);
p(2).Color = [0.8471 0.3216 0.0941];

p(3).LineWidth = 1.5;
p(3).LineStyle = ':';
% p(3).Marker = 'd';
% p(3).MarkerIndices = 1:71:length(f);
p(3).Color = [0.8471 0.3216 0.0941];

p(4).LineWidth = 1.5;
p(4).LineStyle = '-.';
% p(4).Marker = 'd';
% p(4).MarkerIndices = 1:71:length(f);
p(4).Color = [0.8471 0.3216 0.0941];

p(5).LineWidth = 1.5;
p(5).LineStyle = '-';
% p(5).Marker = 's';
% p(5).MarkerIndices = 1:11:length(f);
p(5).Color = [0 0.4470 0.7410];

p(6).LineWidth = 2;
p(6).LineStyle = '--';
% p(6).Marker = 'o';
% p(6).MarkerIndices = 1:51:length(f);
p(6).Color = [0 0.4470 0.7410];

p(7).LineWidth = 1.5;
p(7).LineStyle = ':';
% p(7).Marker = 'd';
% p(7).MarkerIndices = 1:71:length(f);
p(7).Color = [0 0.4470 0.7410];

p(8).LineWidth = 1.5;
p(8).LineStyle = '-.';
% p(8).Marker = 'd';
% p(8).MarkerIndices = 1:71:length(f);
p(8).Color = [0 0.4470 0.7410];

xlabel('Frequency (GHz)');
ylabel('S parameters (dB)');

% legend('S_{11} TE','S_{11} TM', 'S_{21} TE','Location','southeast')
legend(Ids{2}{1},Ids{4}{1},Ids{6}{1},Ids{8}{1},Ids{10}{1},Ids{12}{1},Ids{14}{1},Ids{16}{1},'Location','southeast');
legend('boxoff')

set(gca, 'FontName', 'Times New Roman')
set(gca, 'FontSize', 14)

