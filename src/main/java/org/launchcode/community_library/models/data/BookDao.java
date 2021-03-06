package org.launchcode.community_library.models.data;

import org.launchcode.community_library.models.Book;
import org.springframework.data.repository.CrudRepository;

import org.springframework.stereotype.Repository;
import org.springframework.transaction.annotation.Transactional;

@Repository
@Transactional
public interface BookDao extends CrudRepository<Book, Integer> {
}
