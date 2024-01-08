React.useEffect(() => {
        function watchWidth(){
            console.log("setting up")
            setWindowWidth(window.innerWidth)
    }
        window.addEventListener("resize", watchWidth)

        return function(){
            console.log("cleaning up...")
            window.removeEventListener("resize", watchWidth)
        }
    }, [])

  NOTE that when we turn off the window tracker component(make it false) and run the resize event, we get a warning of a memory leak. this is because we set up an event listener on the window, which registered it with the browser and removing window tracker component doesnt remove that event listener->this results in a side effect/consequences 
  therefore, we need to clean up the effect you have created in the useEffect 

  this is where the return function comes in in useEffect




our App component is deciding when our <WindowTracker/> should be rendered. when it is turned on, it sets the state windowWidth
note that useEffect will only run after the DOM has been painted (once h1 rendered) useEffect has no dependencies as theres nth to reregister a new event. 

THE MOMENT when we toggle off the show state(in App.js), React realises that the WindowTracker component has reached the end of its cycle and will be removed from the DOM, therefore it runs the function it first received when setting up useEffect and runs it, removing the event listener 


ALL IN ALL, this teaches us the clean up fn useEffect has 