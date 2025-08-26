#include <iostream>
#include <string>
#include <vector>
#include <memory>
// #include <concepts>
// using namespace std;


// /* Represents a type in the reflection system. 
// * 元数据类型
// */
// class Type{
//     public:
//         enum class Kind {
//             unknown,
//             Numeric,// Numeric types
//             String, // String type
//             Enum,  // Enum type
//             Class, // Class type
//             Property, // Property type
//         };

//         virtual ~Type() = default;
//         Type(Kind kind) : kind(kind) {}
//         Type(const string &name, Kind kind) : name(name), kind(kind) {}
//         template <typename, typename> friend class TypeInfo;
//         template <typename T>
//             // requires derived_from<T, Type>
//         const T* as() const;

//         string getName() const {
//             return name;
//         }
//         Kind getKind() const {
//             return kind;
//         }

//     private:

//         string name;
//         Kind kind;
// };

// class Numeric : public Type {
//     public:
//         enum class Kind{
//             Unknown,
//             Int8,UInt8,
//             Int16,UInt16,
//             Int32,UInt32,
//             Int64,UInt64,
//             Float,Double,
//         };
//         Kind GetKind() const {return kind;}
//         static string GetNameofKind(Kind kind){
//             switch (kind) {
//                 case Kind::Unknown: return "Unknown";
//                 case Kind::Int8: return "Int8";
//                 case Kind::UInt8: return "UInt8";
//                 case Kind::Int16: return "Int16";
//                 case Kind::UInt16: return "UInt16";
//                 case Kind::Int32: return "Int32";
//                 case Kind::UInt32: return "UInt32";
//                 case Kind::Int64: return "Int64";
//                 case Kind::UInt64: return "UInt64";
//                 case Kind::Float: return "Float";
//                 case Kind::Double: return "Double";
//                 default: return "Unknown";
//             }
//         }

//         Numeric() : Type(Type::Kind::Numeric) {}
//         Numeric(Kind kind) : Type(GetNameofKind(kind),Type::Kind::Numeric), kind(kind) {}

//     private:
//         Kind kind;

// };

// class String : public Type {
//     public:
//         String() : Type(Type::Kind::String) {}
//         String(const string &name) : Type(name, Type::Kind::String) {}
// };


// class Enum : public Type {
//     public:
//         struct Item{
//             using ValueType = int; // or any other type you want to use for enum values
//             string name;
//             ValueType value;
//         };
//         Enum() : Type(Type::Kind::Enum) {}
//         Enum(const string &name) : Type(name, Type::Kind::Enum) {}
//         const vector<Item>& getItems() const {
//             return items;
//         }

//         template <typename T>
//         Enum &Add(const string &name, T value) {
//             items.emplace_back(name, static_cast<Item::ValueType>(value));
//             return *this;
//         }

//     private:
//         vector<Item> items;
// };

// class Class : public Type {
//     public:
//         Class() : Type(Type::Kind::Class) {}
//         Class(const string &name) : Type(name, Type::Kind::Class) {}

//         const vector<shared_ptr<Property>>& getProperties() const {
//             return properties;
//         }
//         Class &AddProperty(shared_ptr<Property> &property) {
//             properties.push_back(property);
//             return *this;
//         }
//     private:
//         vector<shared_ptr<Property>> properties; // Properties of the class
// };


// class Property : public Type {
//     public:
//         Property() : Type(Type::Kind::Property) {}
//         Property(const string &name, shared_ptr<Type> type) : Type(name, Type::Kind::Property), type(type) {}

//     private:
//         shared_ptr<Type> type;
// };


// /**
//  * 类型注册
//  * 
//  */

//  template <typename T>
//  class Singleton {
//     public:
//         static T& Instance() {
//             static T instance;
//             return instance;
//         }

//         Singleton(T &&) = delete;
//         Singleton(const T &) = delete;
//         Singleton& operator=(T &&) = delete;

//     protected:
//         Singleton() = default;
//         virtual ~Singleton() = default;
//  };

// // Primary template declaration for TypeInfo
// template <typename T, typename U = void>
// class TypeInfo;

// // Specialization for <T, Numeric>
// template <typename T>
// class TypeInfo<T, Numeric> : public Singleton<TypeInfo<T, Numeric>> {
// public:
//     TypeInfo &Register(const string &name) {
//         info.name = name;
//         info.kind = Numeric::DetectKind<T>(); 
//         info.isSigned = is_signed_v<T>; 
//         return *this;
//     }
//     void AutoRegister()
//     {
//         info.name = Numeric::GetNameOfKind(info.kind);
//         info.kind = Numeric::DetectKind<T>();
//         info.isSigned = std::is_signed_v<T>;
//     }

//     const Numeric &GetInfo() const { return info; }
// private:
//     Numeric info;
// };
