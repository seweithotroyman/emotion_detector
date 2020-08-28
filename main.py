import nltk

love = ['sayang','cinta','rindu','bahagia']
joy = ['gembira','suka','senang','suka cita','riang']
surprise = ['terkejut','mengherankan','mencengangkan','mengagetkan','menterkejuntukan','keheranan','heran']
anger = ['marah','kemarahan','berang','murka','dongkol']
sadness =['sedih','pilu','sayu','rintih']
fear = ['takut','khawatir','cemas','bimbang']

example_text = 'Beberapa rindu memang harus sembunyi-sembunyi. Bukan untuk disampaikan, hanya untuk dikirimkan lewat doa.'
tokens = nltk.word_tokenize(example_text)
print(tokens)