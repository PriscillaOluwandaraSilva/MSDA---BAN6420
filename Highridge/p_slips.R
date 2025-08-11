# Generate dynamic list of 400 workers
set.seed(123)
names <- paste0("Worker_", 1:400)
salaries <- sample(5000:35000, 400, replace = TRUE)
genders <- sample(c("Male", "Female"), 400, replace = TRUE)
workers <- data.frame(name = names, salary = salaries, gender = genders, stringsAsFactors = FALSE)

# Generate payment slips
for (i in 1:nrow(workers)) {
  name <- workers$name[i]
  salary <- workers$salary[i]
  gender <- workers$gender[i]
  
  level <- "Unassigned"
  if (salary > 10000 & salary < 20000) {
    level <- "A1"
  }
  if (salary > 7500 & salary < 30000 & gender == "Female") {
    level <- "A5-F"
  }
  
  slip <- paste("Payment Slip for", name, "\nSalary: $", salary, "\nGender: ", gender, "\nLevel: ", level, "\n------------------------------\n", sep="")
  writeLines(slip, paste0("sample_output/", name, "_slip.txt"))
}
