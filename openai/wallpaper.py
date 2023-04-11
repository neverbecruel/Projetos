import openai as oi


oi.api_key = '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'


response = oi.Image.create(
    prompt='painting by da vinci',

    n=1,
    size='1024x1024'
)

img_url = response['data'][0]['url']
print(f'img_url: {img_url}')


'''except: 
    response = oi.Image.create(
        prompt='Starry night by Da Vinci',
        n=1,
        size='1024x1024'
    )
    
    img_url = response['data'][0]['url']
    print(f'img_url: {img_url}')

'''
