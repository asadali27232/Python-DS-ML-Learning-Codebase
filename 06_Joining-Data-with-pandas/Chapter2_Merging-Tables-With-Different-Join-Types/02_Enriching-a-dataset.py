import pandas as pd

taglines = pd.read_csv("taglines.csv")
toy_story = pd.read_csv("toy_story.csv")

# Merge the toy_story and taglines tables with a left join
toystory_tag = toy_story.merge(taglines, on="id", how="left")

# Print the rows and shape of toystory_tag
print(toystory_tag)
print(toystory_tag.shape)

# Merge the toy_story and taglines tables with a inner join
toystory_tag = toy_story.merge(taglines, on="id")

# Print the rows and shape of toystory_tag
print(toystory_tag)
print(toystory_tag.shape)
