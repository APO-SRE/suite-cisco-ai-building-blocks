from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.incidents_collection import IncidentsCollection
from ...models.list_incidents_response_400 import ListIncidentsResponse400
from ...models.list_incidents_response_401 import ListIncidentsResponse401
from ...models.list_incidents_response_403 import ListIncidentsResponse403
from ...models.list_incidents_response_404 import ListIncidentsResponse404
from ...models.list_incidents_response_500 import ListIncidentsResponse500
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    limit: Union[Unset, str] = UNSET,
    offset: Union[Unset, str] = UNSET,
    incident_type: Union[Unset, str] = UNSET,
    severity: Union[Unset, str] = UNSET,
    policy_id: Union[Unset, str] = UNSET,
    created_before: Union[Unset, str] = UNSET,
    created_after: Union[Unset, str] = UNSET,
    updated_before: Union[Unset, str] = UNSET,
    updated_after: Union[Unset, str] = UNSET,
    incident_status: Union[Unset, str] = UNSET,
    vendor: Union[Unset, str] = UNSET,
    customer_key: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    order: Union[Unset, str] = UNSET,
    flat: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["limit"] = limit

    params["offset"] = offset

    params["incident_type"] = incident_type

    params["severity"] = severity

    params["policy_id"] = policy_id

    params["created_before"] = created_before

    params["created_after"] = created_after

    params["updated_before"] = updated_before

    params["updated_after"] = updated_after

    params["incident_status"] = incident_status

    params["vendor"] = vendor

    params["customer_key"] = customer_key

    params["fields"] = fields

    params["order"] = order

    params["flat"] = flat

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/incidents",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[
    Union[
        ListIncidentsResponse400,
        ListIncidentsResponse401,
        ListIncidentsResponse403,
        ListIncidentsResponse404,
        ListIncidentsResponse500,
        list["IncidentsCollection"],
    ]
]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = IncidentsCollection.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if response.status_code == 400:
        response_400 = ListIncidentsResponse400.from_dict(response.json())

        return response_400
    if response.status_code == 401:
        response_401 = ListIncidentsResponse401.from_dict(response.json())

        return response_401
    if response.status_code == 403:
        response_403 = ListIncidentsResponse403.from_dict(response.json())

        return response_403
    if response.status_code == 404:
        response_404 = ListIncidentsResponse404.from_dict(response.json())

        return response_404
    if response.status_code == 500:
        response_500 = ListIncidentsResponse500.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[
    Union[
        ListIncidentsResponse400,
        ListIncidentsResponse401,
        ListIncidentsResponse403,
        ListIncidentsResponse404,
        ListIncidentsResponse500,
        list["IncidentsCollection"],
    ]
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    limit: Union[Unset, str] = UNSET,
    offset: Union[Unset, str] = UNSET,
    incident_type: Union[Unset, str] = UNSET,
    severity: Union[Unset, str] = UNSET,
    policy_id: Union[Unset, str] = UNSET,
    created_before: Union[Unset, str] = UNSET,
    created_after: Union[Unset, str] = UNSET,
    updated_before: Union[Unset, str] = UNSET,
    updated_after: Union[Unset, str] = UNSET,
    incident_status: Union[Unset, str] = UNSET,
    vendor: Union[Unset, str] = UNSET,
    customer_key: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    order: Union[Unset, str] = UNSET,
    flat: Union[Unset, str] = UNSET,
) -> Response[
    Union[
        ListIncidentsResponse400,
        ListIncidentsResponse401,
        ListIncidentsResponse403,
        ListIncidentsResponse404,
        ListIncidentsResponse500,
        list["IncidentsCollection"],
    ]
]:
    """List Incidents

     Incidents are a key resource in CloudLock. Incidents are
    triggered by the CloudLock policy engine when a policy's detection
    criteria results in a match in object (document, field, folder, post, or
    file).
    Incidents can be changed manually by a
    user (by updating incidents fields such as status or severity) or
    automatically as objects or events are reevaluated by the policy
    engine. Depending on the incident type, different incident information may be
    available.

    Key information about an incident:
    Summary - Basic incident information and
    status
    Details - Information about the relevant object(s) associated with this incident
    Entity - Information about the object related
    to the incident
    Matches - Matches represent the actual hits
    within the content (for content type policies)

    Args:
        limit (Union[Unset, str]):
        offset (Union[Unset, str]):
        incident_type (Union[Unset, str]):
        severity (Union[Unset, str]):
        policy_id (Union[Unset, str]):
        created_before (Union[Unset, str]):
        created_after (Union[Unset, str]):
        updated_before (Union[Unset, str]):
        updated_after (Union[Unset, str]):
        incident_status (Union[Unset, str]):
        vendor (Union[Unset, str]):
        customer_key (Union[Unset, str]):
        fields (Union[Unset, str]):
        order (Union[Unset, str]):
        flat (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ListIncidentsResponse400, ListIncidentsResponse401, ListIncidentsResponse403, ListIncidentsResponse404, ListIncidentsResponse500, list['IncidentsCollection']]]
    """

    kwargs = _get_kwargs(
        limit=limit,
        offset=offset,
        incident_type=incident_type,
        severity=severity,
        policy_id=policy_id,
        created_before=created_before,
        created_after=created_after,
        updated_before=updated_before,
        updated_after=updated_after,
        incident_status=incident_status,
        vendor=vendor,
        customer_key=customer_key,
        fields=fields,
        order=order,
        flat=flat,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    limit: Union[Unset, str] = UNSET,
    offset: Union[Unset, str] = UNSET,
    incident_type: Union[Unset, str] = UNSET,
    severity: Union[Unset, str] = UNSET,
    policy_id: Union[Unset, str] = UNSET,
    created_before: Union[Unset, str] = UNSET,
    created_after: Union[Unset, str] = UNSET,
    updated_before: Union[Unset, str] = UNSET,
    updated_after: Union[Unset, str] = UNSET,
    incident_status: Union[Unset, str] = UNSET,
    vendor: Union[Unset, str] = UNSET,
    customer_key: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    order: Union[Unset, str] = UNSET,
    flat: Union[Unset, str] = UNSET,
) -> Optional[
    Union[
        ListIncidentsResponse400,
        ListIncidentsResponse401,
        ListIncidentsResponse403,
        ListIncidentsResponse404,
        ListIncidentsResponse500,
        list["IncidentsCollection"],
    ]
]:
    """List Incidents

     Incidents are a key resource in CloudLock. Incidents are
    triggered by the CloudLock policy engine when a policy's detection
    criteria results in a match in object (document, field, folder, post, or
    file).
    Incidents can be changed manually by a
    user (by updating incidents fields such as status or severity) or
    automatically as objects or events are reevaluated by the policy
    engine. Depending on the incident type, different incident information may be
    available.

    Key information about an incident:
    Summary - Basic incident information and
    status
    Details - Information about the relevant object(s) associated with this incident
    Entity - Information about the object related
    to the incident
    Matches - Matches represent the actual hits
    within the content (for content type policies)

    Args:
        limit (Union[Unset, str]):
        offset (Union[Unset, str]):
        incident_type (Union[Unset, str]):
        severity (Union[Unset, str]):
        policy_id (Union[Unset, str]):
        created_before (Union[Unset, str]):
        created_after (Union[Unset, str]):
        updated_before (Union[Unset, str]):
        updated_after (Union[Unset, str]):
        incident_status (Union[Unset, str]):
        vendor (Union[Unset, str]):
        customer_key (Union[Unset, str]):
        fields (Union[Unset, str]):
        order (Union[Unset, str]):
        flat (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ListIncidentsResponse400, ListIncidentsResponse401, ListIncidentsResponse403, ListIncidentsResponse404, ListIncidentsResponse500, list['IncidentsCollection']]
    """

    return sync_detailed(
        client=client,
        limit=limit,
        offset=offset,
        incident_type=incident_type,
        severity=severity,
        policy_id=policy_id,
        created_before=created_before,
        created_after=created_after,
        updated_before=updated_before,
        updated_after=updated_after,
        incident_status=incident_status,
        vendor=vendor,
        customer_key=customer_key,
        fields=fields,
        order=order,
        flat=flat,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    limit: Union[Unset, str] = UNSET,
    offset: Union[Unset, str] = UNSET,
    incident_type: Union[Unset, str] = UNSET,
    severity: Union[Unset, str] = UNSET,
    policy_id: Union[Unset, str] = UNSET,
    created_before: Union[Unset, str] = UNSET,
    created_after: Union[Unset, str] = UNSET,
    updated_before: Union[Unset, str] = UNSET,
    updated_after: Union[Unset, str] = UNSET,
    incident_status: Union[Unset, str] = UNSET,
    vendor: Union[Unset, str] = UNSET,
    customer_key: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    order: Union[Unset, str] = UNSET,
    flat: Union[Unset, str] = UNSET,
) -> Response[
    Union[
        ListIncidentsResponse400,
        ListIncidentsResponse401,
        ListIncidentsResponse403,
        ListIncidentsResponse404,
        ListIncidentsResponse500,
        list["IncidentsCollection"],
    ]
]:
    """List Incidents

     Incidents are a key resource in CloudLock. Incidents are
    triggered by the CloudLock policy engine when a policy's detection
    criteria results in a match in object (document, field, folder, post, or
    file).
    Incidents can be changed manually by a
    user (by updating incidents fields such as status or severity) or
    automatically as objects or events are reevaluated by the policy
    engine. Depending on the incident type, different incident information may be
    available.

    Key information about an incident:
    Summary - Basic incident information and
    status
    Details - Information about the relevant object(s) associated with this incident
    Entity - Information about the object related
    to the incident
    Matches - Matches represent the actual hits
    within the content (for content type policies)

    Args:
        limit (Union[Unset, str]):
        offset (Union[Unset, str]):
        incident_type (Union[Unset, str]):
        severity (Union[Unset, str]):
        policy_id (Union[Unset, str]):
        created_before (Union[Unset, str]):
        created_after (Union[Unset, str]):
        updated_before (Union[Unset, str]):
        updated_after (Union[Unset, str]):
        incident_status (Union[Unset, str]):
        vendor (Union[Unset, str]):
        customer_key (Union[Unset, str]):
        fields (Union[Unset, str]):
        order (Union[Unset, str]):
        flat (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ListIncidentsResponse400, ListIncidentsResponse401, ListIncidentsResponse403, ListIncidentsResponse404, ListIncidentsResponse500, list['IncidentsCollection']]]
    """

    kwargs = _get_kwargs(
        limit=limit,
        offset=offset,
        incident_type=incident_type,
        severity=severity,
        policy_id=policy_id,
        created_before=created_before,
        created_after=created_after,
        updated_before=updated_before,
        updated_after=updated_after,
        incident_status=incident_status,
        vendor=vendor,
        customer_key=customer_key,
        fields=fields,
        order=order,
        flat=flat,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    limit: Union[Unset, str] = UNSET,
    offset: Union[Unset, str] = UNSET,
    incident_type: Union[Unset, str] = UNSET,
    severity: Union[Unset, str] = UNSET,
    policy_id: Union[Unset, str] = UNSET,
    created_before: Union[Unset, str] = UNSET,
    created_after: Union[Unset, str] = UNSET,
    updated_before: Union[Unset, str] = UNSET,
    updated_after: Union[Unset, str] = UNSET,
    incident_status: Union[Unset, str] = UNSET,
    vendor: Union[Unset, str] = UNSET,
    customer_key: Union[Unset, str] = UNSET,
    fields: Union[Unset, str] = UNSET,
    order: Union[Unset, str] = UNSET,
    flat: Union[Unset, str] = UNSET,
) -> Optional[
    Union[
        ListIncidentsResponse400,
        ListIncidentsResponse401,
        ListIncidentsResponse403,
        ListIncidentsResponse404,
        ListIncidentsResponse500,
        list["IncidentsCollection"],
    ]
]:
    """List Incidents

     Incidents are a key resource in CloudLock. Incidents are
    triggered by the CloudLock policy engine when a policy's detection
    criteria results in a match in object (document, field, folder, post, or
    file).
    Incidents can be changed manually by a
    user (by updating incidents fields such as status or severity) or
    automatically as objects or events are reevaluated by the policy
    engine. Depending on the incident type, different incident information may be
    available.

    Key information about an incident:
    Summary - Basic incident information and
    status
    Details - Information about the relevant object(s) associated with this incident
    Entity - Information about the object related
    to the incident
    Matches - Matches represent the actual hits
    within the content (for content type policies)

    Args:
        limit (Union[Unset, str]):
        offset (Union[Unset, str]):
        incident_type (Union[Unset, str]):
        severity (Union[Unset, str]):
        policy_id (Union[Unset, str]):
        created_before (Union[Unset, str]):
        created_after (Union[Unset, str]):
        updated_before (Union[Unset, str]):
        updated_after (Union[Unset, str]):
        incident_status (Union[Unset, str]):
        vendor (Union[Unset, str]):
        customer_key (Union[Unset, str]):
        fields (Union[Unset, str]):
        order (Union[Unset, str]):
        flat (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ListIncidentsResponse400, ListIncidentsResponse401, ListIncidentsResponse403, ListIncidentsResponse404, ListIncidentsResponse500, list['IncidentsCollection']]
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            offset=offset,
            incident_type=incident_type,
            severity=severity,
            policy_id=policy_id,
            created_before=created_before,
            created_after=created_after,
            updated_before=updated_before,
            updated_after=updated_after,
            incident_status=incident_status,
            vendor=vendor,
            customer_key=customer_key,
            fields=fields,
            order=order,
            flat=flat,
        )
    ).parsed
