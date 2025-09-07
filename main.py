import src.parentdetail as parents

def greet(name):
    return f"Hello, {name}!"

if __name__ == "__main__":
    user = input("Enter your name: ")
    print(greet(user))
    
    father,mother = parents.accept_parent_names()
    print(f"Father's Name: {father}, Mother's Name: {mother}" )

