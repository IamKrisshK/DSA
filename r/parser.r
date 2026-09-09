parser<-function(){
  l<-readline(prompt="Enter unsorted array: ")
  arr<-as.integer(strsplit(trimws(l),"\\s+")[[1]])
  return (arr)
}
