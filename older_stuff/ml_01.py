### SCIKIT-LEARN ###
from sklearn.linear_model import LinearRegression

# def weight_culc(hight):
#     return  -64.83 + 0.79 * hight

# guys1 =guys.iloc[:,2:4]

# create X and y
dict_guy = {'Height': pd.Series([100, 40, 55, 6]),
            'Weight': pd.Series([5000, 100, 250, 670])}
guys1 = pd.DataFrame(dict_guy)
guys1
# x = guys1['Height'].reshape(-1,1)
# print(guys1['Height'].head())
# x
# guys1['Height'].head()

# y = guys1['Weight']


# # # instantiate and fit
# lm2 = LinearRegression()
# lm2.fit(x, y)
# lm2.score(x,y)


# # # print the coefficients
# print(lm2.intercept_)
# print(lm2.coef_)

# plt.scatter(x,y, c=np.where(guys.Sex=='m', 'blue', 'pink'))
# plt.plot(x,weight_culc(x), color='g', linewidth=5)

