shaker_sort<-function(arr){
  l<-1
  r<-length(arr)
  while (l<r){
    for(i in l:r){
      if(arr[i]>arr[i+1]){
        t <- arr[i]
        arr[i]<- arr[i+1]
        arr[i+1]<-t
      }
    }
    r<-r-1
    for(j in r:l+1){
      if(arr[j]<arr[j-1]){
        t<-arr[j]
        arr[j]<-arr[j-1]
        arr[j-1]<-t
      }
    }
    l<-l+1}
  return (arr)
}
