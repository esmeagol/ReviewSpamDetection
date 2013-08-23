setwd('F:\\IR\\sentiment_analysis\\mine')
project_dir = getwd()
review_file = 'chhota_part'

library(plyr)
library(stringr)
source( file.path(project_dir, 'sentiment.R') )

pos = scan(file.path(project_dir, 'positive-words.txt'), what='character', comment.char=';')
review=scan(file.path(project_dir, review_file) ,what='character',sep='\n')
Score = score.sentiment(review, pos, .progress='text')
limit memoryuse 3096m
#' write.table(score, pos_score.out)

