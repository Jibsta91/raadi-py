import React, { useEffect, useState } from 'react';
import { View, Text, FlatList } from 'react-native';
import axios from 'axios';

const Home = ({ navigation }) => {
  const [items, setItems] = useState([]);

  useEffect(() => {
    axios.get('/api/items')
      .then(response => {
        setItems(response.data);
      })
      .catch(error => {
        console.error('There was an error fetching the items!', error);
      });
  }, []);

  return (
    <View>
      <Text>Items</Text>
      <FlatList
        data={items}
        keyExtractor={item => item.id}
        renderItem={({ item }) => (
          <Text>{item.name}: {item.description}</Text>
        )}
      />
    </View>
  );
};

export default Home;
