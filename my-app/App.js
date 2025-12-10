import React from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { createNativeStackNavigator } from '@react-navigation/native-stack';

import LoginScreen from './screens/LoginScreen';
import CadastroScreen from './screens/CadastroScreen';
import HomeScreen from './screens/HomeScreen';
import RegistrarFaltaScreen from './screens/RegistrarFaltaScreen';
import EditarFaltaScreen from './screens/EditarFaltaScreen';
import ListaFaltasScreen from './screens/ListaFaltasScreen';

const Stack = createNativeStackNavigator();

export default function App() {
  return (
    <NavigationContainer>
      <Stack.Navigator screenOptions={{ headerTitleAlign: 'center' }}>

        <Stack.Screen name="Login" component={LoginScreen} />
        <Stack.Screen name="Cadastro" component={CadastroScreen} />
        <Stack.Screen name="Home" component={HomeScreen} />
        <Stack.Screen name="ListaFaltas" component={ListaFaltasScreen} />
        <Stack.Screen name="RegistrarFalta" component={RegistrarFaltaScreen} />
        <Stack.Screen name="EditarFalta" component={EditarFaltaScreen} />

      </Stack.Navigator>
    </NavigationContainer>
  );
}
