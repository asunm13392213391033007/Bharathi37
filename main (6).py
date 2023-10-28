def linear_search_product(productlist,targetproduct):
  indices=[]
  for i,product in enumerate(productlist):
    if product == targetproduct:
      indices.append(i)

  return indices
def linear_search_product(productlist,targetproduct):
  indices=[]
  for i,product in enumerate(productlist):
    if product == targetproduct:
      indices.append(i)

  return indices

#Example usage:
products=["avocado","cabbage","eggplant","avocado","cucumber","avocado"]
target="avocado"
result=linear_search_product(products,target)
print(result)