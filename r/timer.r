Timer<-function(){
  start<-proc.time()
  timeit<-function(){
    end<-proc.time()-start
    print(paste("Time taken: ",end))
    start<-proc.time()
  }
  list(timeit=timeit)
}
