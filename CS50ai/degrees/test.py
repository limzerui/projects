names={"clown"}
if "clown" not in names:
    names["clown"] = "19"
else:
    names["clown"].lower().add("19")

print(names)

#if row["name"].lower() not in names:
 #               names[row["name"].lower()] = {row["id"]}
  #          else:
   #             names[row["name"].lower()].add(row["id"])