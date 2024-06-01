
# 1. LOADING IN PACKAGES+OBSERVING DATA
library(tidyverse)
View(starwars)


# 2. FILTERING MISSING DATA
  #is.na
is.na(starwars)
colSums(is.na(starwars))

  #complete.cases, non missing data
filter_na <- starwars %>%
  select(name, gender, hair_color, height) %>%
  filter(!complete.cases(.)) %>% #cancels out no missing data, . entire df
  View()

  
# 3. DEALING WITH MISSING DATA
  #na.omit()
omitted_na <- starwars %>%
  select(name, gender, hair_color, height) %>%
  na.omit() %>% 
  View()

  #drop_na(variable)
dropped_na <- starwars %>%
  select(name, gender, hair_color, height) %>%
  drop_na(height) %>% #cancels out no missing data, . entire df
  View()

  #fill numerical values with mean
starwars$height[is.na(starwars$height)] <- mean(starwars$height, na.rm=TRUE)

filter_na <- starwars %>%
  select(name, gender, hair_color, height) %>%
  filter(!complete.cases(.)) %>% #cancels out to get missing data, . entire df
  View()

  #fill numerical values with a specific value
val_input_na <- starwars %>%
  select(name, gender, hair_color, height) %>%
  mutate(gender = replace_na(gender, "none")) %>%
  View()



