def convert(lst):
    return ' '.join(lst).split()




x = ['hello', 'hi', 'hai', 'hey', 'hello there', 'hi there', 'hey there', 'hello ava', 'hi ava', 'hello ava', 'konichiwa', 'heya', 'bonjor', 'bonjour', 'hola', 'heya ava', 'bonjor ava', 'bonjour ava', 'hola amigo', 'goodbye', 'bye', 'bye bye', 'ba bye', 'i gotta go', 'i have to go now', 'i need to take a leave ava', 'i am leaving', 'i am going ava', 'i am going', 'goodbye ava', 'bye ava', 'bye bye ava', 'babai', 'mayabhai', 'ba bye ava', 'i gotta go ava', 'i have to go now ava', 'i need to take a leave ava', 'i am leaving ava', 'How are you', 'Yo what is up', 'yo yo', 'ayo wadap', 'what about you', 'wassup', 'I am also good', 'I am fine', 'fine', 'good', 'awesome', 'fantastic', 'doing great', 'happy', 'better', 'i am good', 'i am good as always', 'i am doing great', 'i am really good', 'i am okay', 'I am sad', 'i am upset', 'i am feeling kinda low', 'i am feeling low', 'i am messed up', 'i am really messed up', 'i am really messed up right now', 'i am messed up actually', 'i am actually messed up right now', 'very sad', 'sad', 'unhappy', 'feeling low', 'not great', 'not well', 'terrible', ' i am really sad', 'i am really sad right now', 'i am really sad actually', ' i am very sad', 'i am very sad right now', 'i am very sad actually', 'i am sad right now', 'i am sad actually', 'i am really upset', 'i am really upset right now', 'i am really upset actually', 'i am very upset', 'i am very upset right now', 'i am very upset actually', 'i am in trouble', 'can we talk', 'i really need someone to talk to', 'i really need someone to talk', 'i really need someone to listen to me', 'haha', 'hahahaa', 'that was funny', 'very funny', 'good one', 'bad joke', 'trash joke', 'terrible', 'not funny', 'what is your name', 'what should I call you', 'whats your name?', 'your name', 'I hate you', 'you stupid', 'you dumb', 'you mean', 'you my friend', 'I like you', 'I love you', 'you cool', 'you are chill', 'no', 'nah', 'not really', 'thats scary', 'singularity', 'Thanks', 'Thank you', "That's helpful"]
inp = "how are you"
# inp = inp.upper()
# x = str(x).upper()
# x = list(x.split(" "))
lis = list(inp.split(" "))
aset = set(lis)
x = convert(x)
# x = list(x.split(" "))
print(x)
# y = set(x)
# res = aset.intersection(y)
# lis = []
# lis.extend(res)
# print(aset)
# print(y)



    