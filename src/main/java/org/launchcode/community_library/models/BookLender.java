package org.launchcode.community_library.models;

import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.Id;
import javax.persistence.OneToMany;
import java.util.HashSet;
import java.util.Set;

@Entity
public class BookLender {
    @Id
    @GeneratedValue
    private int id;

    @OneToMany(mappedBy="bookLender")
    private Set<Book> lentBooks= new HashSet<Book>();

}
