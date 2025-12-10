import React, { useState } from 'react';
import { View, Text, TextInput, TouchableOpacity, StyleSheet } from 'react-native';

export default function LoginScreen({ navigation }) {
  const [login, setLogin] = useState('');
  const [senha, setSenha] = useState('');

  function entrar() {
    navigation.navigate("Home");
  }

  return (
    <View style={styles.container}>
      <View style={styles.box}>
        <Text style={styles.title}>Login</Text>

        <Text style={styles.label}>Login</Text>
        <TextInput style={styles.input} value={login} onChangeText={setLogin} />

        <Text style={styles.label}>Senha</Text>
        <TextInput 
          style={styles.input} 
          secureTextEntry 
          value={senha} 
          onChangeText={setSenha} 
        />

        <TouchableOpacity style={styles.btn} onPress={entrar}>
          <Text style={styles.btnText}>Entrar</Text>
        </TouchableOpacity>

        <TouchableOpacity onPress={() => navigation.navigate("Cadastro")}>
          <Text style={styles.link}>Cadastrar docente</Text>
        </TouchableOpacity>

        <Text style={styles.info}>
          Caso tenha perdido suas credenciais, contate o administrador.
        </Text>
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: '#F3E5F5' // roxo claro igual ao PDF
  },

  box: {
    width: '85%',
    backgroundColor: '#fff',
    padding: 28,
    borderRadius: 20,
    elevation: 6,
  },

  title: {
    fontSize: 28,
    textAlign: 'center',
    marginBottom: 25,
    fontWeight: 'bold',
    color: '#512DA8' // roxo escuro
  },

  label: {
    marginTop: 10,
    fontWeight: '700',
    color: '#5E35B1'
  },

  input: {
    borderWidth: 2,
    borderColor: '#9575CD',
    borderRadius: 10,
    padding: 12,
    marginTop: 6,
  },

  btn: {
    backgroundColor: '#673AB7',
    padding: 15,
    borderRadius: 12,
    marginTop: 25,
  },

  btnText: {
    color: '#fff',
    textAlign: 'center',
    fontWeight: 'bold',
    fontSize: 16
  },

  link: {
    textAlign: 'center',
    color: '#7E57C2',
    marginTop: 20,
    fontWeight: 'bold',
    fontSize: 14
  },

  info: {
    textAlign: 'center',
    fontSize: 12,
    color: '#6A1B9A',
    marginTop: 10
  }
});
