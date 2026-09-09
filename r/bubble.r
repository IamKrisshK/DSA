bubble_sort<-function(arr){
  n<-length(arr)
  if(n<2){
    return(arr)
  }
  for(i in 1:(n-1)){
    s<- FALSE
    for(j in 1:(n-i)){
      if(arr[j]>arr[j+1]){
        t<-arr[j]
        arr[j]<-arr[j+1]
        arr[j+1]<-t
        s<-TRUE
      }
    }
    if (!s){break}
  }
  return(arr)
}
