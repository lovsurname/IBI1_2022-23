movie_students = {'Comedy': 73, 'Action': 42, 'Romance': 38, 'Fantasy': 28, 'Science-fiction': 22, 'Horror': 19, 'Crime': 18, 'Documentary': 12, 'History': 8, 'War': 7, }
print(movie_students)
import matplotlib.pyplot as plt
import numpy as np
y = np.array([73, 42, 38, 28, 22, 19, 18, 12, 8, 7])
plt.pie(y,
        labels=['Comedy','Action','Romance','Fantasy','Science-fiction','Horror','Crime','Documentary','History','War'],
        )
plt.title("Favourite movie genres among Chinese university students")
plt.show()






