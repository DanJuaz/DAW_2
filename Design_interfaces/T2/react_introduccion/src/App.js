import { useRef } from "react";

const Cats = () => {
  const cat1 = useRef(null);
  const cat2 = useRef(null);
  function handleScrollToFirtsCat() {
    cat1.current.scrollIntoView({
      behavior: "smooth",
      block: "start",
      inline: "center",
    });
  }
  function handleScrollToSecondCat() {
    cat2.current.scrollIntoView({
      behavior: "smooth",
      block: "start",
      inline: "center",
    });
  }
  return (
    <>
      <nav style={{ textAlign: "center" }}>
        <button onClick={handleScrollToFirtsCat()}>ir a Puskas</button>
        <button onClick={handleScrollToSecondCat()}>ir a Wanda</button>
      </nav>
      <div>
        <ul>
          <li style={{ display: "inline", whiteSpace: "nowrap" }}>
            <img
              src="https://placekitten.com/g/200/200"
              ref={cat1}
              alt="Wanda"
            />
          </li>
          <li style={{ display: "inline", whiteSpace: "nowrap" }}>----</li>
          <li style={{ display: "inline", whiteSpace: "nowrap" }}>
            <img
              src="https://placekitten.com/g/300/200"
              ref={cat2}
              alt="Puskas"
            />
          </li>
        </ul>
      </div>
    </>
  );
};

export default Cats;
/*import React, { useEffect, useState } from "react";


const App = () => {
  const [data, setData] = useState([]);
  useEffect(() => {
    const API_URL = 'https://dummyjson.com/users';
    const getUsers = async () => {
      try{
        const response = await fetch(API_URL);
        const data = await response.json();
        setData(data.users);
      }catch(error){
        console.log(error);
      };
    };
    getUsers();
  }, []);
  return (
    <ul>
      {data.map((item => (
        <li id={item.id}>
          <p>{item.firstName} {item.lastName}</p>
        </li>
      )
      ))};
    </ul>
  );
};

/*
export default App;

const App = () => {
  const [cont, setCont] = React.useState(0);
  const increment = () => setCont(cont + 5);
  const decrement = () => setCont(cont - 5);
  const reset = () => setCont(0);
  return (
    <div>
      <p>Paretn Count: {cont}</p>
      <Child count={cont} />
      <div>
        {cont <15 ? (
          <button onClick={increment}>Increment</button>
        ):(
          <p>The Count is in limit</p>
        )}
        <button onClick={decrement}>Decrement</button>
        <button onClick={reset}>Reset</button>
      </div>
    </div>
  ); 
};

const Child = ({count}) => <p>Child Count: {count}</p>;
export default App;
*/
