print("Hello World")
#%%
counties = ['Arapahoe','Denver','Jefferson']
#%%
counties
# %%
type(counties)
# %%
voting_data =[]
voting_data.append({'county':'Arapahoe', 'registered_voters':422829})
voting_data.append({'county':'Denver','registered_voters':463353})
voting_data.append({'county':'Jefferson','registered_voters':432438})
#%%
voting_data
# %%
counties = ['Arapahoe','Denver','Jefferson']
#%%
if counties[1] == 'Denver':
    print(counties[1])
# %%
if 'El Paso' in counties:
    print("El Paso is in the list of counties")
else:
    print('El Paso is not in the list of counties')
#%%
counties_dict = {'Arapahoe':422829,'Denver':463353,'Jefferson':432438}
for county, voters in counties_dict.items():
    print(f'{county} county has {voters:,} registered voters.')
#%%
voting_data = [
    {"county":"Arapahoe", "registered_voters": 422829},
    {"county":"Denver", "registered_voters": 463353},
    {"county":"Jefferson", "registered_voters": 432438}]
#%%
print(voting_data[0])
#%%
def county in voting_data
#%%
for i in range(len(voting_data)):
    print(voting_data[i])
# %%
# trying to define keys:values?
for i in range(len(voting_data)):
    voting_data[i] = {
        "county" : county,
        "voters" : registered_voters
    }
# %%
for element in voting_data:
    print(type(element))
# %%
for keys, values in voting_data[0]:
    county : 'county'
    registered_voters : 'voters'
# stopped trying to define keys/values in dict will come back to it
# %%
