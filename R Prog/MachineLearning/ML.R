
#set working directory
path <- "C:\\Users\\I321790\\R_projects\\MachineLearning"
setwd(path)

#load data and check data
mydata <- read.csv("airfoil_self_noise.csv")
str(mydata)

#check missing values
colSums(is.na(mydata))

#check correlation
cor(mydata)

#In R, the base function lm is used for regression.
regmodel <- lm(Sound_pressure_level ~ .,data=mydata)
summary(regmodel)


#set graphic output
par(mfrow=c(2,2))

#create residual plots
plot(regmodel)

# Among all, Residual vs. Fitted value catches my attention. Not exactly though, 
# but I see signs of heteroskedasticity in this data
# we'll build another model with log(y).
regmodel <- update(regmodel,log(Sound_pressure_level) ~.)
summary(regmodel)
plot(regmodel)
