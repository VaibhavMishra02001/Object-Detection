clc
clear all
close all
caminf=imaqhwinfo;
mycam=char(caminf.InstalledAdaptors());
mycaminfo=imaqhwinfo(mycam)
resolution=char(mycaminfo.DeviceInfo.SupportedFormats());
vid=videoinput(mycam,1,resolution)
set(vid,'FramesPerTrigger',Inf);%keep on taking frames till code is executed
set(vid,'ReturnedColorspace','rgb');
vid.FrameGrabInterval=5
start(vid)
t0=clock;
X=zeros([]);
count1 = 1;
while etime(clock,t0)<50
    data=getsnapshot(vid);
    diff_im=imsubtract(data(:,:,1),rgb2gray(data));
    diff_im=medfilt2(diff_im,[3,3]);
    diff_im=im2bw(diff_im,0.10);
    diff_im=bwareaopen(diff_im,300);
    bw=bwlabel(diff_im,8);
    stats=regionprops(bw,'BoundingBox','Centroid');
    figure(1),imshow(data);
    hold on
    
    for object=1:length(stats)
        bb=stats(object).BoundingBox;
        bc=stats(object).Centroid;
        rectangle('Position',bb,'EdgeColor','r','LineWidth',2)
        plot(bc(1),bc(2),'-m+')
    
        a=text(bc(1)+15,bc(2),bc(3),strcat('X: ',num2str(round(bc(1))),'  Y :',num2str(round(bc(2)))),'Z: ',num2str(round(bc(3))));
        
        X(count1,:)= [round(bc(1)),round(bc(2)),round(bc(3))];
        count1=count1+1;
        plot(X(:,1),X(:,2),'-m+')
       
        set(a,'FontName','Arial','FontWeight','bold','FontSize',12,'Color','yellow');
    end
    hold off   
    disp(X(:,:))
    flushdata(vid);
end


stop(vid)
flushdata(vid)

tpts = [0 length(X)];
tvec = 0:0.01:5;
[q, qd, qdd, pp] = bsplinepolytraj(X,tpts,tvec);
figure
plot(X(1,:),X(2,:),'xb-')
