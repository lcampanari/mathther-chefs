# mathther-chefs
2019 McGill Physics Hackathon project built with Node, React and Python.

## Setup Python assets

1. Go to the `python/assets/lengthFinder/` directory
1. Create a folder called `build`
1. Using the command line run the following:
```
cmake .. -DCMAKE_BUILD_TYPE=Release
make -j4
```

## Setup the website dependencies

Go to the `website/` directory and run `npm install` to install all the dependencies. You only need to do this once.

## Getting Started

On the `website/` directory, run the following to start the development server:

```
npm run dev
```

Open [http://localhost:3000](http://localhost:3000) to view it in the browser.
https://docs.google.com/presentation/d/1RhZr0oT68hhrdSDBsHxSpqMzpNQiVWziS8E9_0KA5BY/edit?usp=sharing
