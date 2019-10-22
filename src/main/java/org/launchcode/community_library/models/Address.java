package org.launchcode.community_library.models;

import javax.persistence.Embeddable;

@Embeddable
public class Address {
    private String street;
    private String zipCode;
    private String country;
    private String city;
    private String phone;
    private String fax;
    private String email;
    private String password;
    public Address(){}
}
