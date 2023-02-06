import requests

MY_KEY = '25f15961a5e94034b5d231627accafec'

END_POINT = 'https://api.spoonacular.com/recipes/random'

params = {
    'number':3,

}
header = {
    'Content-Type':'application/json',
    'x-api-key':MY_KEY,
}

response = requests.get(END_POINT, params=params, headers=header)
response.raise_for_status()
data = response.json()

recipes = data['recipes'][0]['spoonacularSourceUrl']

print(recipes)