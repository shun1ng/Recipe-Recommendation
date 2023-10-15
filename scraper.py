from bs4 import BeautifulSoup
import requests
import time

# modify to take multiple inputs
#ingredient_inputs = input("Please enter ingredients here: ").split(',')
#print(f'Looking for recipes with {ingredient}')

# change tomato

#print(html_text)
class Scraper():
    def find_recipes(self, tag):
        results = []
        #for ingredient in ingredient_inputs:
        web_link = 'https://www.delish.com/search/?q=' + tag
        #print(web_link)
        html_text = requests.get(web_link).text

        soup = BeautifulSoup(html_text, 'lxml')
        recipes = soup.find_all('a', class_ = 'enk2x9t2 css-1jsxw8p epl65fo4')
    
        counter = 0
        for recipe in recipes:
            recipe_link = 'http://www.delish.com' + recipe['href']
            recipe_text = requests.get(recipe_link).text
            soup1 = BeautifulSoup(recipe_text, 'lxml')
            #ingredients = soup1.find_all('li', class_ = 'css-1rmzm7g eno1xhi2')                
            #ingredient_str = ""
            #for ele in ingredients:
            #    ingre = ele.p.text
            #    ingredient_str += ingre
            #    ingredient_str = ingredient_str.replace(',', ' ')
                #ingredient_list = ingredient_str.split(' ')

                #print(ingredient_list)
                #print(inputs)
                #if all(x in ingredient_str for x in tage):
                #if ingredient in ingredient_str:
                    #print(1)
            recipe_name = recipe.find('span', class_ = 'css-13cdu9y e1rluvgc5').text
            figure = recipe.find('div', class_ = '__resp-container lqip css-bc6d9y enk2x9t1').img['data-src'].split('?')[0]
           
            print(figure)
            
            item = {
                'name': recipe_name,
                'link': recipe_link,
           }
                    #with open(f'posts/{index}.txt', 'w') as f:
                    #        f.write(f"Recipe Name: {recipe_name} \n")
                    #        f.write(f'Recipe Link: {recipe_link}')
                    #        print(f'File Saved: {index}')
            counter += 1
            #print(counter)
                #print(results)
            results.append(item)
 
            
            
            break

                #break
        #print(results)
        return results


recipes = Scraper()

recipes.find_recipes('tomato')
    #recipe_text = requests.get(recipe_link).text
    # ingredients = soup.find_all('li', class_ = 'comp mntl-toc__list-item mntl-block')
    #for ingredient in ingredients:
     #   print(ingredient)
    #break


    #for index, job in enumerate(jobs):
    #published_date = job.find('span', class_ = 'sim-posted').span.text
    #    if 'few' in published_date:
#recipe_name = recipes.find('span', class_ = 'css-13cdu9y e1rluvgc5')  #.text.replace(' ', '')
#print(recipe_name)
    #        skills = job.find('span', class_ = 'srp-skills').text.replace(' ', '')
    #        more_info = job.header.h2.a['href']
    #        if unfamiliar_skill not in skills:
    #            with open(f'posts/{index}.txt', 'w') as f:
    #                f.write(f"Company Name: {company_name.strip()} \n")
    #                f.write(f"Required Skiils: {skills.strip()} \n")
    #                f.write(f'More Info: {more_info}')
    #            print(f'File Saved: {index}')
