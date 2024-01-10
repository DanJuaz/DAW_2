import React, {useState} from 'react';

const SearchUser = () =>{
  const [serachText, setSearchText] = useState('');
  return(
    <div>
      <label htmlfor="search">Search User:</label>
      <input
        id="search"
        type="text"
        onChange={e => setSearchText(e.target.value)}
      />
      <p>Searching for: <strong>{serachText}</strong></p>
    </div>
  );
};

export default SearchUser;