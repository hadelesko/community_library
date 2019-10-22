package org.launchcode.community_library.models.data;

import org.launchcode.community_library.models.Member_BookHub;
import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;
import org.springframework.transaction.annotation.Transactional;

@Repository
@Transactional
public interface Member_BookHubDao extends CrudRepository<Member_BookHub,Integer> {
}
