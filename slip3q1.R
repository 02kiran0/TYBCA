 Reverse_Sum=function(n)
{
sum=0
rev=0
while(n>0)
{
r=n%%10
sum=sum+r;
rev=rev*10+r
n=n%/%10 
}
print(paste("sum of digit:",sum))
print(paste("Reverse of number :",rev))
}
n=as.integer(readline(prompt="Enter a number :"))
Reverse_Sum(n)
